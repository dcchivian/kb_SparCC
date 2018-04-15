# -*- coding: utf-8 -*-
import unittest
import os  # noqa: F401
import json  # noqa: F401
import time
import requests

from os import environ
try:
    from ConfigParser import ConfigParser  # py2
except:
    from configparser import ConfigParser  # py3

from pprint import pprint  # noqa: F401

from biokbase.workspace.client import Workspace as workspaceService
from kb_SparCC.kb_SparCCImpl import kb_SparCC
from kb_SparCC.kb_SparCCServer import MethodContext
from kb_SparCC.authclient import KBaseAuth as _KBaseAuth


class kb_SparCCTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = environ.get('KB_AUTH_TOKEN', None)
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('kb_SparCC'):
            cls.cfg[nameval[0]] = nameval[1]
        # Getting username from Auth profile for token
        authServiceUrl = cls.cfg['auth-service-url']
        auth_client = _KBaseAuth(authServiceUrl)
        user_id = auth_client.get_user(token)
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': token,
                        'user_id': user_id,
                        'provenance': [
                            {'service': 'kb_SparCC',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = workspaceService(cls.wsURL)
        cls.serviceImpl = kb_SparCC(cls.cfg)
        cls.scratch = cls.cfg['scratch']
        cls.callback_url = os.environ['SDK_CALLBACK_URL']

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    def getWsClient(self):
        return self.__class__.wsClient

    def getWsName(self):
        if hasattr(self.__class__, 'wsName'):
            return self.__class__.wsName
        suffix = int(time.time() * 1000)
        wsName = "test_kb_SparCC_" + str(suffix)
        ret = self.getWsClient().create_workspace({'workspace': wsName})  # noqa
        self.__class__.wsName = wsName
        return wsName

    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx


    ##############
    # UNIT TESTS #
    ##############

    ### Test 01: simple sparcc run
    #
    # Uncomment to skip this test
    # HIDE @unittest.skip("skipped test_01_sparcc_base")
    def test_01_sparcc_base(self):
        method_name = 'test_01_sparcc_base'
        print ("\n"+('='*(10+len(method_name))))
        print ("RUNNING "+method_name+"()")
        print (('='*(10+len(method_name)))+"\n")

        # upload biom
        BIOM_json_file = os.path.join('data', 'biom', '37A_37B_KAIJU_species.BIOM.json')
        with open (BIOM_json_file, 'r', 0) as BIOM_json_fh:
            BIOM_obj = json.load(BIOM_json_fh)
        provenance = [{}]
        BIOM_info_list = self.getWsClient().save_objects({
            'workspace': self.getWsName(), 
            'objects': [
                {
                    'type': 'Communities.Biom',
                    'data': BIOM_obj,
                    'name': 'test_BIOM_1',
                    'meta': {},
                    'provenance': provenance
                }
            ]})
        [OBJID_I, NAME_I, TYPE_I, SAVE_DATE_I, VERSION_I, SAVED_BY_I, WSID_I, WORKSPACE_I, CHSUM_I, SIZE_I, META_I] = range(11)  # object_info tuple
        BIOM_ref = str(BIOM_info_list[0][WSID_I])+'/'+str(BIOM_info_list[0][OBJID_I])+'/'+str(BIOM_info_list[0][VERSION_I])


        # run sparcc
        params = {
            'workspace_name':            self.ws_info[1],
            'input_biom_ref':            BIOM_ref,
            'abundance_thresh':          1.0,
            'correlation_type':          'sparcc',
            'iterations':                5,
            #'p_vals_flag':               1,
            'p_vals_flag':               0,
            'bootstraps':                10,  # only used if calculate p_vals
            'single_avg_abund_viz_flag': 0,
            'correlation_viz_threshold': 0.25
        }
        result = self.getImpl().run_SparCC(self.getContext(), params)[0]

        pprint('End to end test result:')
        pprint(result)

        self.assertIn('report_name', result)
        self.assertIn('report_ref', result)

        # make sure the report was created and includes the HTML report and download links
        #rep = self.getWsClient().get_objects2({'objects': [{'ref': result['report_ref']}]})['data'][0]['data']
        #self.assertEquals(rep['direct_html_link_index'], 0)
        #self.assertEquals(len(rep['file_links']), 2)
        #self.assertEquals(len(rep['html_links']), 1)
        #self.assertEquals(rep['html_links'][0]['name'], 'report.html')
        pass
