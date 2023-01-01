## Retail-SKU-Selection-Project

-------------------------------------

## General Outlook / Objectives

This project has been constructed with a what-if scenario for the case when a retail/wholesale company (e.g. Ranch 99,  Ralphs, Vons) launches a new small-size convenience store in Mid-Atlantic area. Per my research, on average, small-size supermarkets is likely to stocks items in a range of 5,000 - 10,000 items. 

In this case, I have chosen the worst case which is selecting 5,000 items which can maximize the profits without violating SKU categorical distribution within Mid-Atlantic area. The term itself, SKU, is very cruial in retail market industry because it allows data to be collected on sales. For example, a store can see which items are selling well and which are not based on the scanned SKUs and the POS data without any confusion. SKU allows us to identify conveniently any silight difference in between similar items such as size, brand, and distribution company.

-------------------------------------

* what is SKU? 

SKU aka UPC stands for a Stock Keeping Unit. It is a scnnable bar code, most often seen printed on product labels in a retail store.


-------------------------------------

This project will be divided into four parts in order :

1) Macro-view Trend Analysis (Competitive/Geographical Analysis) -- US vs Mid-Atlantic
2) 5,000 SKU Selection on the basis of statistical approach
3) Categorial Proportion analysis in 5,000 SKU selection
4) Future Improvement & Strategical Planning

-------------------------------------

* Relevant Files:

1) Hana Project Visualization.pbix
- Used PowerBI as a visualization tool
- visualized the findings and analysis with a meaningful story from the reader's perspective
- First two slides heavily focus on the competitive analysis between US territory vs Mid-Atlantic area
- third/fourth slides are composed of all information what I have found from dataset in Mid-Atlantic area

2) Retail SKU Selection Project Python.py
- Used Jupyter Notebook
- Used IQR method to select the SKUs without violating categorical distribution trend (You can see the reason why I chose this method and how I applied to the item selection process in the ppt file, so please read if you are interested)
- Added visualization section with pieplot, barplot, lineplot, and donut chart

3) Mid-Atlantic SKU Selection Presentation.pptx
- Outlook summary of my findings and purpose of this project
- Summarized all the process I applied to this project (Statistical/Inferential/Descriptive Analysis)
- Included my personal thought on future improvement of this work for the future use

---------------------------------

Last but not least, please feel free to comment if you have any new idea to add on this project for the development.
Enjoy and let me know if you have any questions on my work.
