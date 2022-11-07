<h1 align="center">My cyrillic font</h1>

<p align="center">
<img src="medias/logo.png" width="70%"></p>


## Description
This is a training project created to demonstrate the acquired skills.
The service is designed to recognize 10 Cyrillic fonts in images, so that the user can find the desired or similar font, which has a free license.
<p align="center">
<img src="medias/gif.gif" width="100%"></p>


## About project
There were images generated taking into account the contrast of the background and text, which was calculated using the cie76 standard color difference formula.
<p align="center">
<img src="medias/example.png" width="70%"></p>

Pangrams were added to the images for better training of models. Pangrams are short texts containing all the letters of the alphabet. 
<p align="center">
<img src="medias/example2.png" width="70%"></p>

Three neural networks with architectures were trained: LeNet5, ResNet18 and GoogleNet. Jupyter notebooks with learning process are located in 'notebooks/models_*' folders.
<p>The GoogleNet model showed the best results, so it is used in the final version of the service. The model is located in the 'models/' folder</p>

## Technologies
<p align="center">
<img src="medias/technologies.png" width="80%"></p>


## Scheme
<p align="center">
<img src="medias/model.png" width="80%"></p>
