/*
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
*/

module kb_SparCC {
    /*
    A boolean - 0 for false, 1 for true.
        @range (0, 1)
    */
    typedef int bool;

    /* 
    ** The workspace object refs are of form:
    **
    **    objects = ws.get_objects([{'ref': params['workspace_id']+'/'+params['obj_name']}])
    **
    ** "ref" means the entire name combining the workspace id and the object name
    ** "id" is a numerical identifier of the workspace or object, and should just be used for workspace
    ** "name" is a string identifier of a workspace or object.  This is received from Narrative.
    */
    typedef string workspace_name;
    typedef string data_obj_name;
    typedef string data_obj_ref;


    /* SparCC
    ---------

    Correlation Calculation:
    ========================
    SparCC.py example/fake_data.txt -i 5 --cor_file=example/basis_corr/cor_sparcc.out
    SparCC.py example/fake_data.txt -i 5 --cor_file=example/basis_corr/cor_pearson.out -a pearson
    SparCC.py example/fake_data.txt -i 5 --cor_file=example/basis_corr/cor_spearman.out -a spearman

    Pseudo p-value Calculation:
    ===========================
    MakeBootstraps.py example/fake_data.txt -n 100 -t perm_cor_#.txt -p example/pvals/

    SparCC.py example/pvals/permutation_0.txt -i 5 --cor_file=example/pvals/perm_cor_0.txt
    SparCC.py example/pvals/permutation_1.txt -i 5 --cor_file=example/pvals/perm_cor_1.txt
    SparCC.py example/pvals/permutation_2.txt -i 5 --cor_file=example/pvals/perm_cor_2.txt
    SparCC.py example/pvals/permutation_3.txt -i 5 --cor_file=example/pvals/perm_cor_3.txt
    SparCC.py example/pvals/permutation_4.txt -i 5 --cor_file=example/pvals/perm_cor_4.txt
    ...
    SparCC.py example/pvals/permutation_4.txt -i 5 --cor_file=example/pvals/perm_cor_99.txt

    PseudoPvals.py example/basis_corr/cor_sparcc.out example/pvals/perm_cor_#.txt 100 -o example/pvals/pvals.one_sided.txt -t one_sided
    PseudoPvals.py example/basis_corr/cor_sparcc.out example/pvals/perm_cor_#.txt 100 -o example/pvals/pvals.one_sided.txt -t two_sided
    */


    /* FastPar
    ----------

    Correlation Calculation:
    ========================
    fastspar --otu_table fake_data.txt --correlation median_correlation.tsv --covariance median_covariance.tsv
    fastspar --iterations 500 --exclude_iterations 20 --otu_table fake_data.txt --correlation median_correlation.tsv --covariance median_covariance.tsv
    fastspar --threshold 0.2 --otu_table fake_data.txt --correlation median_correlation.tsv --covariance median_covariance.tsv

    Exact p-value Calculation:
    ==========================
    fastspar_bootstrap --otu_table fake_data.txt --number 1000 --prefix bootstrap_counts/fake_data

    parallel fastspar --otu_table {} --correlation bootstrap_correlation/cor_{/} --covariance bootstrap_correlation/cov_{/} -i 5 ::: bootstrap_counts/*

    fastspar_exactpvalues --otu_table fake_data.txt --correlation median_correlation.tsv --prefix bootstrap_correlation/cor_fake_data_ --permutations 1000 --outfile pvalues.tsv

    Threading option: (must be compiled with OpenMP)
    =================
    fastspar --otu_table fake_data.txt --correlation median_correlation.tsv --covariance median_covariance.tsv --iterations 10000 --threads 32

    */



    /* SparCC App Input Params
    */
    typedef structure {
	workspace_name workspace_name;
	data_obj_ref   input_biom_ref;

	float          abundance_thresh;
	string         correlation_type;
	int            iterations;
	bool           p_vals_flag;
	int            bootstraps;

	bool           single_avg_abund_viz_flag;
	float          correlation_viz_thresh;
    } SparCCInputParams;


    /* SparCC App Output
    */
    typedef structure {
        data_obj_name report_name;
        data_obj_ref  report_ref;
    } SparCCOutput;


    /* SparCC Method
    */
    funcdef run_SparCC(SparCCInputParams params)
        returns (SparCCOutput) authentication required;
};
