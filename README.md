<h1 align="center">My cyrillic font</h1>

<p align="center">
<img src="medias/logo.png" width="70%"></p>


## Description
Это учебный проект, который создавался с целью демонстрации полученных навыков. 
Сервис рассчитан на распознавание 10 шрифтов кириллицы на изображениях, так что пользователь сможет найти нужный или похожий шрифт с бесплатной лицензией. 
<p align="center">
<img src="medias/gif.gif" width="100%"></p>


## About project
Были сгенерированы изображения с учетом контраста фона и текста, который высчитывался по формуле цветового отличия стандарта cie76.
<p align="center">
<img src="medias/example.png" width="70%"></p>

Для лучшего обучения моделей на изображения были добавлены панграммы - короткие тексты со всеми буквами алфавита. 
<p align="center">
<img src="medias/example2.png" width="70%"></p>

Были обучены три нейронные сети с архитектурами: LeNet5, ResNet18 и GoogleNet. Jupyter-ноутбуки с процессом обучения находятся в папках notebooks/models_*.
<p>Лучшие результаты показала модель GoogleNet, поэтому она используется в итоговом варианте сервиса. Модель находится в папке models/</p>

## Technologies
<p align="center">
<img src="medias/technologies.png" width="80%"></p>


## Scheme
<p align="center">
<img src="medias/model.png" width="80%"></p>
