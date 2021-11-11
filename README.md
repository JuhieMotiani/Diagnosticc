# Diagnosticc
It is a Covid-19, Pneumonia and Normal Chest X-ray detection Web-App 🖥 where you can detect the X-ray from the given 3 classes, Flask is used to amalgamate backend with the fronted.

<img align=right width="474" alt="Diagnosticc-logo" src="https://user-images.githubusercontent.com/58872872/141322453-7de3c753-944c-47aa-a451-73058aa8117b.png"/>

## Explanation of the Project
- We've trained the Detection model using two algorithms that is CNN and VGG16. We have used CNN model in Web-app because CNN produced an testing accuracy of 95.17% beating VGG16 by 4%.

- The Dataset we've used to train our models is [here](https://drive.google.com/drive/folders/1hQ5ihPKGIdbe8qNwKIwtmlj1yytZiiNE?usp=sharing).

- You can find Colab file to train CNN from here [here](https://github.com/JuhieMotiani/Diagnosticc/blob/main/CNN_Model.ipynb).

- You can find Colab file to train VGG16 from here [here](https://github.com/JuhieMotiani/Diagnosticc/blob/main/VGG16_Model.ipynb).

- After training the model, we have created a Flask Web-Application that can easily diagnose the covid-19, pneumonia and normal from the uploaded chest X-ray image.

## Project Set-up Guidelines
1. Dowload or clone this repo and open it in any IDE like VSCode, PyCharm, etc.
2. Install the required libraries that are neccesary from [requirements.txt](https://github.com/JuhieMotiani/Diagnosticc/blob/main/requirements.) using ``pip install -r requirements.txt``.
4. Go to the file server.py.
5. Run the code ``python server.py``

## Our Results

1) Testing Accuracy and Graph of the CNN-Model:

<img width="400" height="250" alt="CNN-Graph" src="https://user-images.githubusercontent.com/58872872/141325655-97cf5943-b600-47b6-abba-2cee9db9a8b0.png"/>

<img width="250" height="50" alt="CNN Testing Accuracy" src="https://user-images.githubusercontent.com/58872872/141325943-7f7e3c16-bf3d-4f86-a7ae-001fd441bc5d.png"/>

2) Testing Accuracy and Graph of the VGG16-Model:

<img width="400" height="250" alt="VGG16-Graph" src="https://user-images.githubusercontent.com/58872872/141326221-33b5ce79-e368-4e97-b14f-af1eb854945d.png"/>

<img width="250" height="50" alt="VGG16 Testing Accuracy" src="https://user-images.githubusercontent.com/58872872/141326805-a522ec05-7177-49ce-81ac-e16647b8bb27.png"/>

## Video
You can find the video demonstartion of the project from [here](https://github.com/JuhieMotiani/Diagnosticc/blob/main/Implementation%20Video.mp4).

## Facing any issues???
Feel free to [open an issue](https://github.com/juhiemotiani/Diagnosticc/issues/new?assignees=&labels=Query&title=Query). We'll be glad to help you.❤️

## Developers
1. [Juhie Motiani](https://github.com/JuhieMotiani)
2. [Dhruti Patel](https://github.com/iamdhrutipatel)
3. [Anjali Patel](https://github.com/anjali-patel21)
