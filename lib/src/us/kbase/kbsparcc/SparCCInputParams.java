
package us.kbase.kbsparcc;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: SparCCInputParams</p>
 * <pre>
 * SparCC App Input Params
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "workspace_name",
    "input_biom_ref",
    "abundance_thresh",
    "correlation_type",
    "iterations",
    "p_vals_flag",
    "bootstraps",
    "single_avg_abund_viz_flag",
    "correlation_viz_thresh"
})
public class SparCCInputParams {

    @JsonProperty("workspace_name")
    private String workspaceName;
    @JsonProperty("input_biom_ref")
    private String inputBiomRef;
    @JsonProperty("abundance_thresh")
    private Double abundanceThresh;
    @JsonProperty("correlation_type")
    private String correlationType;
    @JsonProperty("iterations")
    private Long iterations;
    @JsonProperty("p_vals_flag")
    private Long pValsFlag;
    @JsonProperty("bootstraps")
    private Long bootstraps;
    @JsonProperty("single_avg_abund_viz_flag")
    private Long singleAvgAbundVizFlag;
    @JsonProperty("correlation_viz_thresh")
    private Double correlationVizThresh;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("workspace_name")
    public String getWorkspaceName() {
        return workspaceName;
    }

    @JsonProperty("workspace_name")
    public void setWorkspaceName(String workspaceName) {
        this.workspaceName = workspaceName;
    }

    public SparCCInputParams withWorkspaceName(String workspaceName) {
        this.workspaceName = workspaceName;
        return this;
    }

    @JsonProperty("input_biom_ref")
    public String getInputBiomRef() {
        return inputBiomRef;
    }

    @JsonProperty("input_biom_ref")
    public void setInputBiomRef(String inputBiomRef) {
        this.inputBiomRef = inputBiomRef;
    }

    public SparCCInputParams withInputBiomRef(String inputBiomRef) {
        this.inputBiomRef = inputBiomRef;
        return this;
    }

    @JsonProperty("abundance_thresh")
    public Double getAbundanceThresh() {
        return abundanceThresh;
    }

    @JsonProperty("abundance_thresh")
    public void setAbundanceThresh(Double abundanceThresh) {
        this.abundanceThresh = abundanceThresh;
    }

    public SparCCInputParams withAbundanceThresh(Double abundanceThresh) {
        this.abundanceThresh = abundanceThresh;
        return this;
    }

    @JsonProperty("correlation_type")
    public String getCorrelationType() {
        return correlationType;
    }

    @JsonProperty("correlation_type")
    public void setCorrelationType(String correlationType) {
        this.correlationType = correlationType;
    }

    public SparCCInputParams withCorrelationType(String correlationType) {
        this.correlationType = correlationType;
        return this;
    }

    @JsonProperty("iterations")
    public Long getIterations() {
        return iterations;
    }

    @JsonProperty("iterations")
    public void setIterations(Long iterations) {
        this.iterations = iterations;
    }

    public SparCCInputParams withIterations(Long iterations) {
        this.iterations = iterations;
        return this;
    }

    @JsonProperty("p_vals_flag")
    public Long getPValsFlag() {
        return pValsFlag;
    }

    @JsonProperty("p_vals_flag")
    public void setPValsFlag(Long pValsFlag) {
        this.pValsFlag = pValsFlag;
    }

    public SparCCInputParams withPValsFlag(Long pValsFlag) {
        this.pValsFlag = pValsFlag;
        return this;
    }

    @JsonProperty("bootstraps")
    public Long getBootstraps() {
        return bootstraps;
    }

    @JsonProperty("bootstraps")
    public void setBootstraps(Long bootstraps) {
        this.bootstraps = bootstraps;
    }

    public SparCCInputParams withBootstraps(Long bootstraps) {
        this.bootstraps = bootstraps;
        return this;
    }

    @JsonProperty("single_avg_abund_viz_flag")
    public Long getSingleAvgAbundVizFlag() {
        return singleAvgAbundVizFlag;
    }

    @JsonProperty("single_avg_abund_viz_flag")
    public void setSingleAvgAbundVizFlag(Long singleAvgAbundVizFlag) {
        this.singleAvgAbundVizFlag = singleAvgAbundVizFlag;
    }

    public SparCCInputParams withSingleAvgAbundVizFlag(Long singleAvgAbundVizFlag) {
        this.singleAvgAbundVizFlag = singleAvgAbundVizFlag;
        return this;
    }

    @JsonProperty("correlation_viz_thresh")
    public Double getCorrelationVizThresh() {
        return correlationVizThresh;
    }

    @JsonProperty("correlation_viz_thresh")
    public void setCorrelationVizThresh(Double correlationVizThresh) {
        this.correlationVizThresh = correlationVizThresh;
    }

    public SparCCInputParams withCorrelationVizThresh(Double correlationVizThresh) {
        this.correlationVizThresh = correlationVizThresh;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((((((((((((((((((("SparCCInputParams"+" [workspaceName=")+ workspaceName)+", inputBiomRef=")+ inputBiomRef)+", abundanceThresh=")+ abundanceThresh)+", correlationType=")+ correlationType)+", iterations=")+ iterations)+", pValsFlag=")+ pValsFlag)+", bootstraps=")+ bootstraps)+", singleAvgAbundVizFlag=")+ singleAvgAbundVizFlag)+", correlationVizThresh=")+ correlationVizThresh)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
