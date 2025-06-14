# Hand-Gesture-Minecraft-Controller
A pre trained Mediapipe Machine Learning model that detects your hand gestures like closed fist, thumb down, etc, and according to that, moves your Minecraft player.

## Setup
You can clone the repository using  ```git clone https://github.com/Aruniaaa/Hand-Gesture-Minecraft-Controller.git
cd Hand-Gesture-Minecraft-Controller ```

You can also download the requirements using ``` pip install opencv-python mediapipe keyboard numpy ``` if you haven't already.

## Usage
To use this, you have to open VSCode, or any other code editor/IDE you use in administrator mode, this is really important since your IDE won't be able to press the neccessary keys to move otherwise.
After that, simply run this script and you should see the webcam window popping up, if it doesn't consider changing line 68 of minecraft-player.py to a different camera if you have it.
Next, you can open minecraft (although this should work for any other game which follows WASD for moving and Space for jumping), and simply control the player using your webcam and hand gestures.

Here are the instructions on what each gesture does - 
1. Closed fist ✊ -> Moving forward (W)
2. Open palm ✋ -> Moving backwards (S)
3. Pointing up with your index finger ☝️ -> Jump (Space)
4. Thumbs up 👍 -> Moving left (A)
5. Thumbs down 👎 -> Moving right (D)
6. Victory ✌️ -> Stop all movements (this doesn't permanently stop your player, you can move again by the above mentioned gestures)
   

NOTE - You can not use two hand gestures at a time, so for something like jumping and walking forward you will have to do that with your keyboard. This program also doesn't support camera rotation, which you will manually have to do, of course you can modify this version to support all of the above and use it, or even send a pull request!<3

With that said, I do really hope you enjoy this!!! 

Made by -> Arunia 



