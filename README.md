# Daegu Apartment Price Predictor
## **Background**  
Daegu’s urban landscape faces increasing housing demands due to limited residential land availability and concentrated commercial activity. Apartments serve as a critical housing solution, with pricing influenced by multiple internal and external factors.  

---

## **Problem Statement**  
Current apartment pricing practices present challenges for property owners:  
- **Price Determination Complexity**  
  - Owners and real estate companies set unit prices independently when listing on platforms.  
  - Market-aligned pricing requires continuous monitoring of dynamic conditions.  
- **Pricing Accuracy Risks**  
  - Overpriced units experience extended time-on-market and reduced buyer interest.  
  - Underpriced units sacrifice potential profit margins.  
- **Market Responsiveness Gap**  
  - Manual price adjustments lag behind rapid market fluctuations.  
  - Limited access to comprehensive pricing benchmarks creates valuation uncertainty.  

This situation creates a need for **data-driven pricing tools** that balance market competitiveness with optimal returns.  

---

## **Project Objectives**  
1. **Develop a Predictive Pricing Model**  
   - Build a machine learning model to estimate Daegu apartment prices based on key factors.  
   - Achieve a minimum **R² ≥ 80%** to ensure reliable price explanations.  
2. **Improve Pricing Accuracy**  
   - Reduce prediction errors to **< ₩40,000 MAE** for competitive yet profitable listings.  
   - Minimize **MAPE to < 20%** for consistent pricing guidance.  
3. **Provide Actionable Insights**  
   - Generate clear pricing recommendations for owners.  

---

## **Stakeholders**  
### **Primary Stakeholders (Direct Users)**  
- **Apartment Owners**  
  - *Need*: Prevent profit loss from incorrect pricing.  
  - *Benefit*: Science-backed price guidance balancing competitiveness and returns.  
- **Real Estate Agents**  
  - *Need*: Credible valuations to justify prices to clients.  
  - *Benefit*: Automated comps and market analytics.  

### **Secondary Stakeholders (Platform Partners)**  
- **Property Listing Platforms**  
  - *Need*: Accurate listings to maintain user trust.  
  - *Benefit*: Reduced price disputes and faster transactions.  

### **Tertiary Stakeholders (Public Sector)**  
- **Local Government**  
  - *Need*: Housing market visibility.  
  - *Benefit*: Data for affordability monitoring and policy-making.  

---

## **Model Performance Evaluation**  
1. **80% Price Factor Coverage (R²)**  
   - The model captures **80% of measurable factors** influencing Daegu apartment prices.  
   - The remaining 20% depends on unique property characteristics.  
2. **Typical Price Estimate Accuracy**  
   - **Average error**: ±₩37,800 (Mean Absolute Error).  
   - **Example**: For a ₩200 million apartment, estimates typically fall between **₩162–238 million**.  
3. **Maximum Expected Variance**  
   - **Worst-case error margin**: ±₩47,000 (Root Mean Square Error).  
   - **95% of estimates** remain within this range of actual market value.  
4. **Percentage Variance Guidance**  
   - **Average 19% variance** (Mean Absolute Percentage Error).  
   - **Recommended pricing strategy**:  
     - Use model estimates as baseline.  
     - Apply **±20% adjustment buffer**.  

---

## **Business Interpretation**  
The pricing model demonstrates strong predictive capability with the following key characteristics:  
1. **High Explanatory Power**  
   - Captures majority of factors influencing Daegu apartment prices.  
2. **Controlled Error Margins**  
   - Maintains an **18% average price variation**.  
3. **Market-Adaptive Performance**  
   - Performs optimally for standard-priced properties.  
4. **Practical Implementation Benefits**  
   - Enables data-supported pricing decisions.  

---

## **Limitations & Recommendations**  
### **Model Limitations to Note**  
1. **Market Responsiveness**  
   - Requires periodic manual adjustments for rapid demand changes.  
2. **Data Dependencies**  
   - Accuracy depends on timely and complete property data.  
3. **Neighborhood Specifics**  
   - May underweight emerging developments or seasonal fluctuations.  

### **Future Enhancement Opportunities**  
1. **Model Optimization**  
   - Implement **Bayesian Optimization** for precision.  
2. **Feature Expansion**  
   - Add **crime statistics, walkability scores, and transportation access**.  
3. **Data Quality Improvements**  
   - Prioritize **daily updates** and advanced error correction.  

### **Implementation Guidance**  
- Best used as a **core pricing reference**.  
- Combine with:  
  - Professional appraisals.  
  - Neighborhood comps.  
  - Owner’s market knowledge.  

---

### **Conclusion**  
This predictive model enables **optimized rental pricing** through data-driven recommendations, actionable insights, and transparent metrics. While effective for standard properties, luxury units may require supplemental adjustments. Future enhancements will focus on improving accuracy and expanding features.  

---

### **Requirements**  

- streamlit 
- pandas
- scikit-learn==1.4.2
