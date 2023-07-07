# 24-7-Pharmacist



## Content

[Important facts before running the code](#important)

[About](#about) 

[How to run](#how) 

<a name="important"/>

## Important facts before running the code

<a name="about"/>

## About



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
