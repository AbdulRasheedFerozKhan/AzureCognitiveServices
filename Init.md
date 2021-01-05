```python
pip install --upgrade pip
```

    Collecting pip
      Downloading pip-20.3.3-py2.py3-none-any.whl (1.5 MB)
    [K     |████████████████████████████████| 1.5 MB 7.6 MB/s eta 0:00:01
    [?25hInstalling collected packages: pip
      Attempting uninstall: pip
        Found existing installation: pip 20.1.1
        Uninstalling pip-20.1.1:
          Successfully uninstalled pip-20.1.1
    Successfully installed pip-20.3.3
    Note: you may need to restart the kernel to use updated packages.



```python
pip install numpy==1.18.5
```

    Requirement already satisfied: numpy==1.18.5 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (1.18.5)
    Note: you may need to restart the kernel to use updated packages.



```python
pip install xlrd==1.2.0
```

    Collecting xlrd==1.2.0
      Downloading xlrd-1.2.0-py2.py3-none-any.whl (103 kB)
    [K     |████████████████████████████████| 103 kB 7.2 MB/s eta 0:00:01
    [?25hInstalling collected packages: xlrd
    Successfully installed xlrd-1.2.0
    Note: you may need to restart the kernel to use updated packages.



```python
pip install pandas==1.0.4
```

    Collecting pandas==1.0.4
      Downloading pandas-1.0.4-cp36-cp36m-manylinux1_x86_64.whl (10.1 MB)
    [K     |████████████████████████████████| 10.1 MB 6.5 MB/s eta 0:00:01
    [?25hRequirement already satisfied: numpy>=1.13.3 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from pandas==1.0.4) (1.18.5)
    Requirement already satisfied: python-dateutil>=2.6.1 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from pandas==1.0.4) (2.8.1)
    Requirement already satisfied: pytz>=2017.2 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from pandas==1.0.4) (2020.4)
    Requirement already satisfied: six>=1.5 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from python-dateutil>=2.6.1->pandas==1.0.4) (1.15.0)
    Installing collected packages: pandas
      Attempting uninstall: pandas
        Found existing installation: pandas 0.25.3
        Uninstalling pandas-0.25.3:
          Successfully uninstalled pandas-0.25.3
    [31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
    azureml-train-automl-runtime 1.19.0 requires pandas<1.0.0,>=0.21.0, but you have pandas 1.0.4 which is incompatible.
    azureml-opendatasets 1.19.0 requires pandas<=1.0.0,>=0.21.0, but you have pandas 1.0.4 which is incompatible.
    azureml-opendatasets 1.19.0 requires scipy<=1.4.1,>=1.0.0, but you have scipy 1.5.2 which is incompatible.
    azureml-automl-runtime 1.19.0 requires pandas<1.0.0,>=0.21.0, but you have pandas 1.0.4 which is incompatible.[0m
    Successfully installed pandas-1.0.4
    Note: you may need to restart the kernel to use updated packages.



```python
pip install scikit-learn==0.23.1
```

    Collecting scikit-learn==0.23.1
      Downloading scikit_learn-0.23.1-cp36-cp36m-manylinux1_x86_64.whl (6.8 MB)
    [K     |████████████████████████████████| 6.8 MB 7.5 MB/s eta 0:00:01
    [?25hRequirement already satisfied: scipy>=0.19.1 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from scikit-learn==0.23.1) (1.5.2)
    Requirement already satisfied: threadpoolctl>=2.0.0 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from scikit-learn==0.23.1) (2.1.0)
    Requirement already satisfied: joblib>=0.11 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from scikit-learn==0.23.1) (0.14.1)
    Requirement already satisfied: numpy>=1.13.3 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from scikit-learn==0.23.1) (1.18.5)
    Installing collected packages: scikit-learn
      Attempting uninstall: scikit-learn
        Found existing installation: scikit-learn 0.22.2.post1
        Uninstalling scikit-learn-0.22.2.post1:
          Successfully uninstalled scikit-learn-0.22.2.post1
    [31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
    azureml-train-automl-runtime 1.19.0 requires pandas<1.0.0,>=0.21.0, but you have pandas 1.0.4 which is incompatible.
    azureml-train-automl-runtime 1.19.0 requires scikit-learn<0.23.0,>=0.19.0, but you have scikit-learn 0.23.1 which is incompatible.
    azureml-automl-runtime 1.19.0 requires pandas<1.0.0,>=0.21.0, but you have pandas 1.0.4 which is incompatible.
    azureml-automl-runtime 1.19.0 requires scikit-learn<0.23.0,>=0.19.0, but you have scikit-learn 0.23.1 which is incompatible.[0m
    Successfully installed scikit-learn-0.23.1
    Note: you may need to restart the kernel to use updated packages.



```python
pip install keras==2.3.1
```

    Requirement already satisfied: keras==2.3.1 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (2.3.1)
    Requirement already satisfied: pyyaml in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from keras==2.3.1) (5.3.1)
    Requirement already satisfied: h5py in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from keras==2.3.1) (2.10.0)
    Requirement already satisfied: six>=1.9.0 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from keras==2.3.1) (1.15.0)
    Requirement already satisfied: keras-preprocessing>=1.0.5 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from keras==2.3.1) (1.1.2)
    Requirement already satisfied: scipy>=0.14 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from keras==2.3.1) (1.5.2)
    Requirement already satisfied: numpy>=1.9.1 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from keras==2.3.1) (1.18.5)
    Requirement already satisfied: keras-applications>=1.0.6 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from keras==2.3.1) (1.0.8)
    Note: you may need to restart the kernel to use updated packages.



```python
pip install tensorflow==2.0.0
```

    Collecting tensorflow==2.0.0
      Downloading tensorflow-2.0.0-cp36-cp36m-manylinux2010_x86_64.whl (86.3 MB)
    [K     |████████████████████████████████| 86.3 MB 40 kB/s  eta 0:00:01
    [?25hRequirement already satisfied: astor>=0.6.0 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from tensorflow==2.0.0) (0.8.1)
    Requirement already satisfied: keras-preprocessing>=1.0.5 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from tensorflow==2.0.0) (1.1.2)
    Requirement already satisfied: absl-py>=0.7.0 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from tensorflow==2.0.0) (0.11.0)
    Requirement already satisfied: termcolor>=1.1.0 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from tensorflow==2.0.0) (1.1.0)
    Requirement already satisfied: wrapt>=1.11.1 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from tensorflow==2.0.0) (1.12.1)
    Requirement already satisfied: wheel>=0.26 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from tensorflow==2.0.0) (0.35.1)
    Requirement already satisfied: keras-applications>=1.0.8 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from tensorflow==2.0.0) (1.0.8)
    Requirement already satisfied: numpy<2.0,>=1.16.0 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from tensorflow==2.0.0) (1.18.5)
    Requirement already satisfied: protobuf>=3.6.1 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from tensorflow==2.0.0) (3.14.0)
    Requirement already satisfied: opt-einsum>=2.3.2 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from tensorflow==2.0.0) (3.3.0)
    Requirement already satisfied: six>=1.10.0 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from tensorflow==2.0.0) (1.15.0)
    Requirement already satisfied: google-pasta>=0.1.6 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from tensorflow==2.0.0) (0.2.0)
    Requirement already satisfied: grpcio>=1.8.6 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from tensorflow==2.0.0) (1.34.0)
    Collecting gast==0.2.2
      Downloading gast-0.2.2.tar.gz (10 kB)
    Requirement already satisfied: h5py in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from keras-applications>=1.0.8->tensorflow==2.0.0) (2.10.0)
    Collecting tensorboard<2.1.0,>=2.0.0
      Downloading tensorboard-2.0.2-py3-none-any.whl (3.8 MB)
    [K     |████████████████████████████████| 3.8 MB 85.1 MB/s eta 0:00:01
    [?25hRequirement already satisfied: markdown>=2.6.8 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from tensorboard<2.1.0,>=2.0.0->tensorflow==2.0.0) (3.3.3)
    Requirement already satisfied: werkzeug>=0.11.15 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from tensorboard<2.1.0,>=2.0.0->tensorflow==2.0.0) (1.0.1)
    Requirement already satisfied: setuptools>=41.0.0 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from tensorboard<2.1.0,>=2.0.0->tensorflow==2.0.0) (50.3.0.post20201006)
    Requirement already satisfied: google-auth<2,>=1.6.3 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from tensorboard<2.1.0,>=2.0.0->tensorflow==2.0.0) (1.23.0)
    Requirement already satisfied: google-auth-oauthlib<0.5,>=0.4.1 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from tensorboard<2.1.0,>=2.0.0->tensorflow==2.0.0) (0.4.2)
    Requirement already satisfied: requests<3,>=2.21.0 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from tensorboard<2.1.0,>=2.0.0->tensorflow==2.0.0) (2.25.0)
    Requirement already satisfied: rsa<5,>=3.1.4 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from google-auth<2,>=1.6.3->tensorboard<2.1.0,>=2.0.0->tensorflow==2.0.0) (4.6)
    Requirement already satisfied: pyasn1-modules>=0.2.1 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from google-auth<2,>=1.6.3->tensorboard<2.1.0,>=2.0.0->tensorflow==2.0.0) (0.2.8)
    Requirement already satisfied: cachetools<5.0,>=2.0.0 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from google-auth<2,>=1.6.3->tensorboard<2.1.0,>=2.0.0->tensorflow==2.0.0) (4.1.1)
    Requirement already satisfied: requests-oauthlib>=0.7.0 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from google-auth-oauthlib<0.5,>=0.4.1->tensorboard<2.1.0,>=2.0.0->tensorflow==2.0.0) (1.3.0)
    Requirement already satisfied: importlib-metadata in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from markdown>=2.6.8->tensorboard<2.1.0,>=2.0.0->tensorflow==2.0.0) (3.1.1)
    Requirement already satisfied: pyasn1<0.5.0,>=0.4.6 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from pyasn1-modules>=0.2.1->google-auth<2,>=1.6.3->tensorboard<2.1.0,>=2.0.0->tensorflow==2.0.0) (0.4.8)
    Requirement already satisfied: chardet<4,>=3.0.2 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from requests<3,>=2.21.0->tensorboard<2.1.0,>=2.0.0->tensorflow==2.0.0) (3.0.4)
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from requests<3,>=2.21.0->tensorboard<2.1.0,>=2.0.0->tensorflow==2.0.0) (1.25.11)
    Requirement already satisfied: certifi>=2017.4.17 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from requests<3,>=2.21.0->tensorboard<2.1.0,>=2.0.0->tensorflow==2.0.0) (2020.12.5)
    Requirement already satisfied: idna<3,>=2.5 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from requests<3,>=2.21.0->tensorboard<2.1.0,>=2.0.0->tensorflow==2.0.0) (2.10)
    Requirement already satisfied: oauthlib>=3.0.0 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from requests-oauthlib>=0.7.0->google-auth-oauthlib<0.5,>=0.4.1->tensorboard<2.1.0,>=2.0.0->tensorflow==2.0.0) (3.1.0)
    Collecting tensorflow-estimator<2.1.0,>=2.0.0
      Downloading tensorflow_estimator-2.0.1-py2.py3-none-any.whl (449 kB)
    [K     |████████████████████████████████| 449 kB 104.5 MB/s eta 0:00:01
    [?25hRequirement already satisfied: zipp>=0.5 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from importlib-metadata->markdown>=2.6.8->tensorboard<2.1.0,>=2.0.0->tensorflow==2.0.0) (3.4.0)
    Building wheels for collected packages: gast
      Building wheel for gast (setup.py) ... [?25ldone
    [?25h  Created wheel for gast: filename=gast-0.2.2-py3-none-any.whl size=7540 sha256=9f097b7a84eaa4f590727fe0c9d654ac7669e40c673a03aa839347e57909aa54
      Stored in directory: /home/azureuser/.cache/pip/wheels/19/a7/b9/0740c7a3a7d1d348f04823339274b90de25fbcd217b2ee1fbe
    Successfully built gast
    Installing collected packages: tensorflow-estimator, tensorboard, gast, tensorflow
      Attempting uninstall: tensorflow-estimator
        Found existing installation: tensorflow-estimator 2.3.0
        Uninstalling tensorflow-estimator-2.3.0:
          Successfully uninstalled tensorflow-estimator-2.3.0
      Attempting uninstall: tensorboard
        Found existing installation: tensorboard 2.4.0
        Uninstalling tensorboard-2.4.0:
          Successfully uninstalled tensorboard-2.4.0
      Attempting uninstall: gast
        Found existing installation: gast 0.3.3
        Uninstalling gast-0.3.3:
          Successfully uninstalled gast-0.3.3
      Attempting uninstall: tensorflow
        Found existing installation: tensorflow 2.3.1
        Uninstalling tensorflow-2.3.1:
          Successfully uninstalled tensorflow-2.3.1
    [31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
    tensorflow-gpu 2.1.0 requires scipy==1.4.1; python_version >= "3", but you have scipy 1.5.2 which is incompatible.
    tensorflow-gpu 2.1.0 requires tensorboard<2.2.0,>=2.1.0, but you have tensorboard 2.0.2 which is incompatible.
    tensorflow-gpu 2.1.0 requires tensorflow-estimator<2.2.0,>=2.1.0rc0, but you have tensorflow-estimator 2.0.1 which is incompatible.[0m
    Successfully installed gast-0.2.2 tensorboard-2.0.2 tensorflow-2.0.0 tensorflow-estimator-2.0.1
    Note: you may need to restart the kernel to use updated packages.



```python
pip install joblib==0.15.1
```

    Collecting joblib==0.15.1
      Downloading joblib-0.15.1-py3-none-any.whl (298 kB)
    [K     |████████████████████████████████| 298 kB 8.3 MB/s eta 0:00:01
    [?25hInstalling collected packages: joblib
      Attempting uninstall: joblib
        Found existing installation: joblib 0.14.1
        Uninstalling joblib-0.14.1:
          Successfully uninstalled joblib-0.14.1
    [31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
    azureml-train-automl-runtime 1.19.0 requires pandas<1.0.0,>=0.21.0, but you have pandas 1.0.4 which is incompatible.
    azureml-train-automl-runtime 1.19.0 requires scikit-learn<0.23.0,>=0.19.0, but you have scikit-learn 0.23.1 which is incompatible.
    azureml-automl-runtime 1.19.0 requires joblib==0.14.1, but you have joblib 0.15.1 which is incompatible.
    azureml-automl-runtime 1.19.0 requires pandas<1.0.0,>=0.21.0, but you have pandas 1.0.4 which is incompatible.
    azureml-automl-runtime 1.19.0 requires scikit-learn<0.23.0,>=0.19.0, but you have scikit-learn 0.23.1 which is incompatible.[0m
    Successfully installed joblib-0.15.1
    Note: you may need to restart the kernel to use updated packages.



```python
pip install nltk==3.4.5
```

    Collecting nltk==3.4.5
      Downloading nltk-3.4.5.zip (1.5 MB)
    [K     |████████████████████████████████| 1.5 MB 12.0 MB/s eta 0:00:01
    [?25hRequirement already satisfied: six in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from nltk==3.4.5) (1.15.0)
    Building wheels for collected packages: nltk
      Building wheel for nltk (setup.py) ... [?25ldone
    [?25h  Created wheel for nltk: filename=nltk-3.4.5-py3-none-any.whl size=1449904 sha256=6a709ac265011114f7d8f1baaa35a42169f19aa9fe1799e6a6f072e399e8501b
      Stored in directory: /home/azureuser/.cache/pip/wheels/e3/c9/b0/ed26a73ef75a53145820825afa8e2d2c9b30fe9f6c10cd3202
    Successfully built nltk
    Installing collected packages: nltk
    Successfully installed nltk-3.4.5
    Note: you may need to restart the kernel to use updated packages.



```python
pip install gensim==3.8.3
```

    Requirement already satisfied: gensim==3.8.3 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (3.8.3)
    Requirement already satisfied: smart-open>=1.8.1 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from gensim==3.8.3) (1.9.0)
    Requirement already satisfied: six>=1.5.0 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from gensim==3.8.3) (1.15.0)
    Requirement already satisfied: numpy>=1.11.3 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from gensim==3.8.3) (1.18.5)
    Requirement already satisfied: scipy>=0.18.1 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from gensim==3.8.3) (1.5.2)
    Requirement already satisfied: boto3 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from smart-open>=1.8.1->gensim==3.8.3) (1.15.18)
    Requirement already satisfied: requests in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from smart-open>=1.8.1->gensim==3.8.3) (2.25.0)
    Requirement already satisfied: boto>=2.32 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from smart-open>=1.8.1->gensim==3.8.3) (2.49.0)
    Requirement already satisfied: jmespath<1.0.0,>=0.7.1 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from boto3->smart-open>=1.8.1->gensim==3.8.3) (0.10.0)
    Requirement already satisfied: s3transfer<0.4.0,>=0.3.0 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from boto3->smart-open>=1.8.1->gensim==3.8.3) (0.3.3)
    Requirement already satisfied: botocore<1.19.0,>=1.18.18 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from boto3->smart-open>=1.8.1->gensim==3.8.3) (1.18.18)
    Requirement already satisfied: urllib3<1.26,>=1.20 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from botocore<1.19.0,>=1.18.18->boto3->smart-open>=1.8.1->gensim==3.8.3) (1.25.11)
    Requirement already satisfied: python-dateutil<3.0.0,>=2.1 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from botocore<1.19.0,>=1.18.18->boto3->smart-open>=1.8.1->gensim==3.8.3) (2.8.1)
    Requirement already satisfied: certifi>=2017.4.17 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from requests->smart-open>=1.8.1->gensim==3.8.3) (2020.12.5)
    Requirement already satisfied: chardet<4,>=3.0.2 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from requests->smart-open>=1.8.1->gensim==3.8.3) (3.0.4)
    Requirement already satisfied: idna<3,>=2.5 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from requests->smart-open>=1.8.1->gensim==3.8.3) (2.10)
    Note: you may need to restart the kernel to use updated packages.



```python
pip install onnxmltools==1.6.1
```

    Collecting onnxmltools==1.6.1
      Downloading onnxmltools-1.6.1-py2.py3-none-any.whl (293 kB)
    [K     |████████████████████████████████| 293 kB 17.7 MB/s eta 0:00:01
    [?25hRequirement already satisfied: skl2onnx in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from onnxmltools==1.6.1) (1.4.9)
    Requirement already satisfied: onnx in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from onnxmltools==1.6.1) (1.7.0)
    Requirement already satisfied: numpy in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from onnxmltools==1.6.1) (1.18.5)
    Requirement already satisfied: onnxconverter-common<1.7.0,>=1.5.0 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from onnxmltools==1.6.1) (1.6.0)
    Requirement already satisfied: keras2onnx in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from onnxmltools==1.6.1) (1.6.0)
    Requirement already satisfied: six in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from onnxmltools==1.6.1) (1.15.0)
    Requirement already satisfied: protobuf in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from onnxmltools==1.6.1) (3.14.0)
    Requirement already satisfied: fire in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from keras2onnx->onnxmltools==1.6.1) (0.3.1)
    Requirement already satisfied: requests in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from keras2onnx->onnxmltools==1.6.1) (2.25.0)
    Requirement already satisfied: termcolor in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from fire->keras2onnx->onnxmltools==1.6.1) (1.1.0)
    Requirement already satisfied: typing-extensions>=3.6.2.1 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from onnx->onnxmltools==1.6.1) (3.7.4.3)
    Requirement already satisfied: certifi>=2017.4.17 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from requests->keras2onnx->onnxmltools==1.6.1) (2020.12.5)
    Requirement already satisfied: chardet<4,>=3.0.2 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from requests->keras2onnx->onnxmltools==1.6.1) (3.0.4)
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from requests->keras2onnx->onnxmltools==1.6.1) (1.25.11)
    Requirement already satisfied: idna<3,>=2.5 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from requests->keras2onnx->onnxmltools==1.6.1) (2.10)
    Requirement already satisfied: scikit-learn>=0.19 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from skl2onnx->onnxmltools==1.6.1) (0.23.1)
    Requirement already satisfied: threadpoolctl>=2.0.0 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from scikit-learn>=0.19->skl2onnx->onnxmltools==1.6.1) (2.1.0)
    Requirement already satisfied: scipy>=0.19.1 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from scikit-learn>=0.19->skl2onnx->onnxmltools==1.6.1) (1.5.2)
    Requirement already satisfied: joblib>=0.11 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from scikit-learn>=0.19->skl2onnx->onnxmltools==1.6.1) (0.15.1)
    Installing collected packages: onnxmltools
      Attempting uninstall: onnxmltools
        Found existing installation: onnxmltools 1.4.1
        Uninstalling onnxmltools-1.4.1:
          Successfully uninstalled onnxmltools-1.4.1
    [31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
    azureml-train-automl-runtime 1.19.0 requires onnxmltools==1.4.1, but you have onnxmltools 1.6.1 which is incompatible.
    azureml-train-automl-runtime 1.19.0 requires pandas<1.0.0,>=0.21.0, but you have pandas 1.0.4 which is incompatible.
    azureml-train-automl-runtime 1.19.0 requires scikit-learn<0.23.0,>=0.19.0, but you have scikit-learn 0.23.1 which is incompatible.
    azureml-automl-runtime 1.19.0 requires joblib==0.14.1, but you have joblib 0.15.1 which is incompatible.
    azureml-automl-runtime 1.19.0 requires onnxmltools==1.4.1, but you have onnxmltools 1.6.1 which is incompatible.
    azureml-automl-runtime 1.19.0 requires pandas<1.0.0,>=0.21.0, but you have pandas 1.0.4 which is incompatible.
    azureml-automl-runtime 1.19.0 requires scikit-learn<0.23.0,>=0.19.0, but you have scikit-learn 0.23.1 which is incompatible.[0m
    Successfully installed onnxmltools-1.6.1
    Note: you may need to restart the kernel to use updated packages.



```python
pip install keras2onnx==1.6.1
```

    Collecting keras2onnx==1.6.1
      Downloading keras2onnx-1.6.1-py3-none-any.whl (220 kB)
    [K     |████████████████████████████████| 220 kB 20.0 MB/s eta 0:00:01
    [?25hRequirement already satisfied: fire in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from keras2onnx==1.6.1) (0.3.1)
    Requirement already satisfied: onnx in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from keras2onnx==1.6.1) (1.7.0)
    Requirement already satisfied: onnxconverter-common<1.7.0,>=1.6.0 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from keras2onnx==1.6.1) (1.6.0)
    Requirement already satisfied: requests in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from keras2onnx==1.6.1) (2.25.0)
    Requirement already satisfied: numpy in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from keras2onnx==1.6.1) (1.18.5)
    Requirement already satisfied: protobuf in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from keras2onnx==1.6.1) (3.14.0)
    Requirement already satisfied: six in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from onnxconverter-common<1.7.0,>=1.6.0->keras2onnx==1.6.1) (1.15.0)
    Requirement already satisfied: termcolor in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from fire->keras2onnx==1.6.1) (1.1.0)
    Requirement already satisfied: typing-extensions>=3.6.2.1 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from onnx->keras2onnx==1.6.1) (3.7.4.3)
    Requirement already satisfied: chardet<4,>=3.0.2 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from requests->keras2onnx==1.6.1) (3.0.4)
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from requests->keras2onnx==1.6.1) (1.25.11)
    Requirement already satisfied: certifi>=2017.4.17 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from requests->keras2onnx==1.6.1) (2020.12.5)
    Requirement already satisfied: idna<3,>=2.5 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from requests->keras2onnx==1.6.1) (2.10)
    Installing collected packages: keras2onnx
      Attempting uninstall: keras2onnx
        Found existing installation: keras2onnx 1.6.0
        Uninstalling keras2onnx-1.6.0:
          Successfully uninstalled keras2onnx-1.6.0
    [31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
    azureml-train-automl-runtime 1.19.0 requires keras2onnx<=1.6.0,>=1.4.0, but you have keras2onnx 1.6.1 which is incompatible.
    azureml-train-automl-runtime 1.19.0 requires onnxmltools==1.4.1, but you have onnxmltools 1.6.1 which is incompatible.
    azureml-train-automl-runtime 1.19.0 requires pandas<1.0.0,>=0.21.0, but you have pandas 1.0.4 which is incompatible.
    azureml-train-automl-runtime 1.19.0 requires scikit-learn<0.23.0,>=0.19.0, but you have scikit-learn 0.23.1 which is incompatible.
    azureml-automl-runtime 1.19.0 requires joblib==0.14.1, but you have joblib 0.15.1 which is incompatible.
    azureml-automl-runtime 1.19.0 requires keras2onnx<=1.6.0,>=1.4.0, but you have keras2onnx 1.6.1 which is incompatible.
    azureml-automl-runtime 1.19.0 requires onnxmltools==1.4.1, but you have onnxmltools 1.6.1 which is incompatible.
    azureml-automl-runtime 1.19.0 requires pandas<1.0.0,>=0.21.0, but you have pandas 1.0.4 which is incompatible.
    azureml-automl-runtime 1.19.0 requires scikit-learn<0.23.0,>=0.19.0, but you have scikit-learn 0.23.1 which is incompatible.[0m
    Successfully installed keras2onnx-1.6.1
    Note: you may need to restart the kernel to use updated packages.



```python
pip install onnxruntime==1.3.0
```

    Requirement already satisfied: onnxruntime==1.3.0 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (1.3.0)
    Requirement already satisfied: protobuf in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from onnxruntime==1.3.0) (3.14.0)
    Requirement already satisfied: onnx>=1.2.3 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from onnxruntime==1.3.0) (1.7.0)
    Requirement already satisfied: numpy>=1.16.6 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from onnxruntime==1.3.0) (1.18.5)
    Requirement already satisfied: six in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from onnx>=1.2.3->onnxruntime==1.3.0) (1.15.0)
    Requirement already satisfied: typing-extensions>=3.6.2.1 in /anaconda/envs/azureml_py36/lib/python3.6/site-packages (from onnx>=1.2.3->onnxruntime==1.3.0) (3.7.4.3)
    Note: you may need to restart the kernel to use updated packages.



```python

```
