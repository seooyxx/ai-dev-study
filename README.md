# [GDG on Campus KU] branch/junior/ai 
[한국어](README.md)

 GDG on Campus KU의 주니어 대상 AI 강의 `🌳branch/junior/ai` (2024.10.1-2023.11.26)의 관리를 위한 레포지토리입니다. 강의 자료 업로드 및 과제 제출을 목적으로 사용합니다. 

## Repository 활용 방법
* 매주 강의에서 다룰 코드는 강의 시간 전에 [Schedule](##Schedule)에 업데이트 될 예정입니다.
* 모든 수강생은 본 레포지토리를 포크해서 작업해 주세요.

## Scope
* ML/DL 개념 기초 (Loss, Optimizer 등)
* Regularization Technique, Data Augmentation
* CNN 기반 모델 (VGG, ResNet)
* Transformer 기반 모델
* Huggingface 사용법
* 모델 서빙 기초 (GCP, FastAPI, Docker, ONNX)

## Attendances and Homeworks

* 출석은 각 `week-n` 실습 혹은 과제 제출을 기준으로 체크합니다. 대면/비대면 참석 여부는 체크하지 않으나, 모든 강의별로 안내되는 실습 혹은 과제를 `week-(n+1)`수업 직전까지 완료해야 합니다.


## Schedule
* `🌳branch/junior/ai` 는 **매주 화요일 PM 7~9** 대면으로 진행됩니다.
* 대면 장소 및 비대면 참여 방식은 디스코드를 통해 공지됩니다.

| **Week**        | **날짜**       | **시간**       | **내용**                                                   | **강의 자료**  | **과제**  |
|-----------------|----------------|----------------|------------------------------------------------------------|----------------|-----------|
| week-1          | 10.1           | 19:00-21:30    | ML/DL Basics and PyTorch Introduction                      | [Link]()       | [Link]()  |
| week-2          | 10.8           | 19:00-21:30    | Regularization Technique, MLP, Custom DataLoader | [Link]()       | [Link]()  |
| week-3          | 10.29          | 19:00-21:30    | CNN 기반 모델(VGG16, ResNet), Image Classification       | [Link]()       | [Link]()  |
| week-4          | 11.5           | 19:00-21:30    | Vanilla Transformer / Huggingface 사용법                    | [Link]()       | [Link]()  |
| week-5          | 11.12          | 19:00-21:30    | Model Serving 1 : Fastapi, Docker (1)                      | [Link]()       | [Link]()  |
| week-6          | 11.19          | 19:00-21:30    | Model Serving 2 : Fastapi, Docker (2)                      | [Link]()       | [Link]()  |
| pull-requests   | 11.19 → 11.26  |                | Junior → Member 승급전 과제                                   | [Link]()       | [Link]()  |


## Additional Study Materials
이 스터디는 딥러닝의 모든 중요한 부분을 다루지는 않기 때문에, [CS231n](https://cs231n.stanford.edu/) 과 같은 강의로부터 추가 학습 커리큘럼을 제안합니다. 아래 자료는 CS231n의 자료로서, 스터디에서 전부 커버하지 않은 딥러닝의 기본적인 원리 및 구조에 대한 내용을 상세하게 다룹니다. 스터디에서는 아래 내용의 일부가 강의 자료에 포함되어 있습니다.

| **Topic**                           | **Slide**                                                                                           | **Lecture**                                                                                             |
|-------------------------------------|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| Python/Numpy Tutorial                |                            | [tutorial](https://cs231n.github.io/python-numpy-tutorial)                |
| Image Classification                | [slide](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture2.pdf)                            | [lecture](https://www.youtube.com/watch?v=vT1JzLTH4G4&list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv)                |
| Loss Functions and Optimization      | [slide](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture3.pdf)                            | [lecture](https://www.youtube.com/watch?v=h7iBpEHGVNc&list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv)                |
| Deep Learning Software              | [slide](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture8.pdf)                            | [lecture](https://www.youtube.com/watch?v=6SlgtELqOWc&list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv)                |
| Introduction to Neural Networks      | [slide](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture4.pdf)                            | [lecture](https://www.youtube.com/watch?v=d14TUNcbn1k&list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv)                |
| Training Neural Networks, part 1     | [slide](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture6.pdf)                            | [lecture](https://www.youtube.com/watch?v=wEoyxE0GP2M&list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv)                |
| Training Neural Networks, part 2     | [slide](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture7.pdf)                            | [lecture](https://www.youtube.com/watch?v=wEoyxE0GP2M&list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv)                |
| Convolutional Neural Networks        | [slide](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture5.pdf)                            | [lecture](https://www.youtube.com/watch?v=bNb2fEVKeEo&list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv)                |
| CNN Architectures                    | [slide](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture9.pdf)                            | [lecture](https://www.youtube.com/watch?v=DAOcjicFr1Y&list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv)                |
| Detection and Segmentation           | [slide](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture11.pdf)                           | [lecture](https://www.youtube.com/watch?v=nDPWywWRIRo&list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv)                |
| Generative Models                    | [slide](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture13.pdf)                           | [lecture](https://www.youtube.com/watch?v=5WoItGTWV54&list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv)                |
| Introduction to Transformers         |                                                                                                    | [lecture](https://www.youtube.com/watch?v=XfpMkf4rD6E)     

## References
* CS231n
                                                  |