# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os
import json

from kb_SparCC.Utils.SparCCUtil import SparCCUtil
#END_HEADER


class kb_SparCC:
    '''
    Module Name:
    kb_SparCC

    Module Description:
    A KBase module: kb_SparCC
This SDK module is developed to wrap the open source package SparCC
determines correlation values between OTU, taxonomic, or functional structure for microbial communities

References: 
SparCC Homepage: https://bitbucket.org/yonatanf/sparcc
SparCC paper: Friedman J, Alm EJ. (2012) Inferring Correlation Networks from Genomic Survey Data. PLoS Comput Biol. 2012;8(9):e1002687

http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002687
https://doi.org/10.1371/journal.pcbi.1002687
https://www.ncbi.nlm.nih.gov/pubmed/23028285

FastSpar: https://github.com/scwatts/fastspar
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/dcchivian/kb_SparCC"
    GIT_COMMIT_HASH = "4a01c7c1c20031fe292c7d731d2f698879b27946"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.config = config
        self.config['SDK_CALLBACK_URL'] = os.environ['SDK_CALLBACK_URL']
        self.config['KB_AUTH_TOKEN'] = os.environ['KB_AUTH_TOKEN']
        #END_CONSTRUCTOR
        pass


    def run_SparCC(self, ctx, params):
        """
        SparCC Method
        :param params: instance of type "SparCCInputParams" (SparCC App Input
           Params) -> structure: parameter "workspace_name" of type
           "workspace_name" (** The workspace object refs are of form: ** ** 
           objects = ws.get_objects([{'ref':
           params['workspace_id']+'/'+params['obj_name']}]) ** ** "ref" means
           the entire name combining the workspace id and the object name **
           "id" is a numerical identifier of the workspace or object, and
           should just be used for workspace ** "name" is a string identifier
           of a workspace or object.  This is received from Narrative.),
           parameter "input_biom_ref" of type "data_obj_ref", parameter
           "abundance_thresh" of Double, parameter "correlation_type" of
           String, parameter "iterations" of Long, parameter "p_vals_flag" of
           type "bool" (A boolean - 0 for false, 1 for true. @range (0, 1)),
           parameter "bootstraps" of Long, parameter
           "single_avg_abund_viz_flag" of type "bool" (A boolean - 0 for
           false, 1 for true. @range (0, 1)), parameter
           "correlation_viz_thresh" of Double
        :returns: instance of type "SparCCOutput" (SparCC App Output) ->
           structure: parameter "report_name" of type "data_obj_name",
           parameter "report_ref" of type "data_obj_ref"
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN run_SparCC
        print('--->\nRunning kb_SparCC.run_SparCC\nparams:')
        print(json.dumps(params, indent=1))

        sparccUtil_client = SparCCUtil(self.config, ctx)
        returnVal = sparccUtil_client.run_SparCC_with_Pvalue(params)
        #END run_SparCC

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method run_SparCC return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
