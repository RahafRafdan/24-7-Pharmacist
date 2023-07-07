# 24-7-Pharmacist



## Content

[Important facts before running the code](#important)

[About](#about) 

[How to run](#how) 

<a name="important"/>

## Important facts before running the code

This bot has been trained on [the Clinical Questions Collection provided by the National Library of Medicine](https://datadiscovery.nlm.nih.gov/Literature/Clinical-Questions-Collection/i3a4-n4ma?_gl=1*1i1z9ut*_ga*MjAyOTIxODE4NS4xNjg4NTA5ODgz*_ga_P1FPTH9PL4*MTY4ODUwOTg4My4xLjAuMTY4ODUwOTg4My4wLjAuMA..*_ga_7147EPK006*MTY4ODUwOTg4My4xLjAuMTY4ODUwOTg4My4wLjAuMA), as well as selected articles about Metformin which is  used for treating type 2 diabetes. Therefore, for the best answers, please ask questions related to the of Metformin medicine.

<a name="about"/>

## About

This demo offers a virtual experience that simulates a pharmacist's role in assisting patients with inquiries about potential food or medication conflicts for their medications. With this innovative platform, patients can receive personalized recommendations and advice from a virtual pharmacist, which can help them make informed decisions about their health. This can be especially useful for patients who have a complex medication regimen or who may have a history of adverse drug reactions. By using this technology, patients can feel more empowered and confident in managing their health and can have peace of mind knowing that they have a trusted source of information and support at their fingertips.

<a name="how"/>

## How to run 


clone the current repository by 

```
git clone https://github.com/Lama-Alsaif/24-7-Pharmacist.git
```

It is recommended to creating a venv environment by going to the repository path and opening up the terminal type 

```
python -m venv .venv
```
this creates an .venv folder where the new environment will be stored 

then type

``` 
&env/Scripts/Activate.ps1
```

or if the above command did not work type

```
env/Scripts/activate.bat
```
this will activate the environment and you should see the (.venv) at the begging of your command line.

then download the required libraries   
```
 pip install -r requirements.txt
```

If you run into a problem in this step related to hnswlib you will need to download https://visualstudio.microsoft.com/visual-cpp-build-tools/

then navigate to "Individual components", and find these two

![enter image description here](https://i.stack.imgur.com/W67kU.png)

and Windows 10 SDK

![enter image description here](https://i.stack.imgur.com/RHmKX.png)

finaly 

run 
```
streamlit run src/app.py
```

This will open up the webpage of the demo on a new tab
