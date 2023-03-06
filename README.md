# Plant-Pathology

![PP1](https://user-images.githubusercontent.com/88246010/223158664-2ff5e910-b5bf-42a2-820d-78b55a8613a8.gif)

It is a deep learning project used to detect the diseases in a plant leaf. It is trained on around 1800 images having four different categories they are 'Healthy', 'Scab', 'Rust' and 'Multiple Diseases'.


**Data Source**

[KAGGLE](https://www.kaggle.com/competitions/plant-pathology-2020-fgvc7)

**Motivation**

Plant pathology is a critical field in agriculture that deals with the study of plant diseases and their management. Plant diseases can lead to significant yield losses and reduce the quality of agricultural products. The motivation behind this project is to develop a deep learning model that can accurately diagnose plant diseases, enabling farmers to take timely and appropriate measures to prevent or control the spread of diseases.

**Built with**

1. Pandas
2. Numpy
3. Matplotlib
4. Seaborn
5. Flask
6. Opencv

**Usage**

* Before the following steps make sure you have [git](https://git-scm.com/download), [Anaconda](https://www.anaconda.com/) or [miniconda](https://docs.conda.io/en/latest/miniconda.html) installed on your system

* Clone the complete project with ```git clone https://github.com/Prabhanshu-08/Plant-Pathology.git``` or you can just download the code and unzip it.

```
conda create -n plant_pathology python=3.9.6
pip install -r requirements.txt
conda activate plant_pathology 
```

* And finally run the project with
```python app.py```

* Open the localhost url provided after running app.py and now you can use the project locally in your web browser.

**DEMO**

* Home Page

![image](https://user-images.githubusercontent.com/88246010/223166561-fabb6cad-4c98-458b-b232-f9b72bcc0242.png)

If Leaf if 'Healthy'

![image](https://user-images.githubusercontent.com/88246010/223166807-3d6cf9d9-2a42-4b4c-a677-342f29f22902.png)

If Leaf has some disease

![image](https://user-images.githubusercontent.com/88246010/223167029-e978695e-291c-4645-8169-e49d94181aee.png)


**Further Improvements**
1. The model achieved an accuracy of around 85% on test data. This accuracy can be further improved to make project more dependable.
2. Some detailed cure can be provided in case the leaf has some disease.

**Contact**

If you have any doubt or want to contribute feel free to email me or hit me up on [LinkedIn](https://www.linkedin.com/in/prabhanshu-gupta-71248118a/
)
