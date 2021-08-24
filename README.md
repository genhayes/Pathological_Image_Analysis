# Pathological Image Analysis 


## Structure
All functions can be found in MAIN_Functions.py

Scripts starting with many_ loop through batches of files.

Scripts starting with MAIN are the final pipelines.

## Abstract
To overcome current limitations in the simultaneous analysis of immunohistochemistry stains in a single tissue section, 
we have assessed the novel implementation of segmentation and template matching methods sensitive to a range of detectable 
stain and cell patterns. A new double staining technique for urothelial carcinoma samples allows for the visual distinction 
of GATA-binding protein 3 (GATA3) which stains brown, and keratin 5 (KRT5) which stains red. The objective of the algorithms 
is to correctly classify cells based on their staining patterns as KRT5+/GATA3+, KRT5+/GATA3-, KRT5-/GATA3+ or KRT5-/GATA3-. 
After applying preprocessing and colour segmentation, a watershed-based algorithm was found to classify the KRT5 and GATA3 
positivity simultaneously with comparable accuracy and precision to the current gold standard pathological image analysis 
software, HALO. A multi-template matching method and combined method were also assessed and found to have comparable cell 
phenotype classification ratios as HALO for each sample. The template matching method under classifies some cells, but does so 
consistently across all samples, illustrating similar percent phenotyping of cells as with HALO. The accuracy of the template 
matching in the red-stained KRT5+ regions was noticeably lower due to less intensity contrast between the nuclei and cytoplasm 
in heavily red-stained regions. This motivated the development of a combined method which implements the watershed segmentation 
in the red KRT5+ regions and template matching in the uncoloured KRT5- regions. The consistent non-classification of KRT5- 
cells that differ from the templates was still apparent in the combined method; however, with improved template selection and 
variability, the combined method may serve to play each method to its strengths. Through visual assessment by pathologists, 
HALO was found to consistently over classify KRT5+/GATA3- cells which are characteristic of MIBC and rare in NMIBC. This over 
classification was not apparent in any of the other implemented methods. While the segmentation and subtyping algorithms presented 
here cannot substitute analysis from medical professionals, they may provide insights for tissue samples to be assessed more 
efficiently and accurately. Our preliminary results suggested these methods could be further improved by comparing all methods to 
classification ground-truths, implementing more rigorous preprocessing steps, and enhancing template matching methods with feature 
matching.
