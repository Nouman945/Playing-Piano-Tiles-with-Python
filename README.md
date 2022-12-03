## Playing-Piano-Tiles-with-Python Bot

Using python to play piano tiles game. A fun Project for Beginners !!

## Dependencies

This game is tested and working with python version 3.7

Create the conda Enviroment Using 

```
conda create -n piano_tiles python=3.7
```

Activate the Enviroment Using

```
conda activate piano_tiles
```
And install the required dependencies using

```
pip install -r requirements.txt
```

## How to Run the game

Open the game in your browser and copy the x & y location of each block and update the x,y values in the code in following sections

---
```
# 1st Block
if pyautogui.pixel(x1,y1)[0] == 0:
    click(x1,y1) 
# 2nd Block
if pyautogui.pixel(x2,y2)[0] == 0:
    click(x2,y2)
# 3rd Block
if pyautogui.pixel(x3,y3)[0] == 0:
    click(x3,y3)
# 4th Block
if pyautogui.pixel(x4,y4)[0] == 0:
    click(x4,y4)
```

## Given in the image 

<p align="center">
  <img width="460" height="500" src="https://user-images.githubusercontent.com/50593062/117713072-9b411a80-b1ee-11eb-8ce8-452a5dfd44e8.jpg">
</p>

Congrats !! Enjoy Your New Bot player 😉
