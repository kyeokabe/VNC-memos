##1 Introduction

* Consider an example of classifying an image of a digit into a digit
* Handcrafted rules leads to proliferation of rules and of exceptions to the rules leading to poor results
* One good way is to *learn* a function y(x) which maps input x (image of digit) into the corresponding digit    
* The ability to categorize a new sample correctly is called *generalization*
* Most practical applications preprocess input variables  
* This makes solving a problem easy and efficient
* **Supervised learning**: training data comprises examples of the input vectors along with corresponding target vectors  
* **Classification**: assign input vector to finite **discrete** categories
* e.g. digit recognition  
* **Regression**    : assign input vector to **continuous** output  
* e.g. predict chemical raction yeild given inputs of concentrations of reactants, temperatures, pressures, etc.  

* **Unsupervised learning**: training data comprises input vectors x without any corresponding target vectors  
* Typical objectives of unsupervised learning: 
* **1. clustering**: Discover groups of similar examples within the data  
* **2. density estimation**: Determine the distribution of data within the input space
* **3. visualization**: Project the data from a high dimensional space down to two or three dimensions  

* This chapter introduces three important tools: 
* **1. Probability Theory**  
* **2. Decision Theory**  
* **3. Information Theory**  

  
**1.1 Example: Polynomial Curve Fitting**  
**1.2 Probablity Theory**  
**1.2.1 Probability Densities**  


**1.4 The Curse of Dimensionality**  
  
* Practical data: high dimensionality & many input variables
* Fig. 1.19: Want to classify "X". Intuition tells us to classify to near labbels (=green or red)
* Fig. 1.20: input space divided into cells based on majority number of representations
* Fig. 1.19 & 1.20 was a 2D example. **As D increases, the number of regular grids grows exponentially.**
* Not all intuitions developen in spaces of low dimensionality will generalize to spaces of high dimensionality  
* e.g. Fig. 1.22: Fraction of the volume of a sphere lying in the surface increases as dimensionality D increases  
* The dimensionality curse does not precent us from finding effective techniques qpplicable to high dimensional space  
* why? Two reasons:  
* Reason 1: Real data usually is confined in a lower effective dimensionality
* Reason 2: Often in real data, small change in input variable will produce changes in the target variable  
* Succesful pattern recognition techniques exploit these two properties  
* 
