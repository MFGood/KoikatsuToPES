# KoikatsuToPES
Blender addon to convert Koikatsu vertex groups to PES ones

Made to be used with models exported from [KKBP](https://github.com/FlailingFog/KK-Blender-Porter-Pack) into [Blender 2.79](https://www.blender.org/download/releases/2-79/) for use with [PES FMDL Blender](https://github.com/the4chancup/pes-fmdl-blender)

# Usage
When using KKBP, during the "Prep for target application" step, make sure you select "No changes (FAST)" and "Generic FBX - No changes" as seen below; if you don't use these settings, the exported .fbx file may not have the correct vertex groups and the addon will error out. <br>
![image](https://user-images.githubusercontent.com/98861097/209112451-6783f0b4-d8b4-48c8-a49d-1ef423e6f7df.png) <br>
When it comes time to rename and mix weights on vertex groups, press Space and run this instead: <br>
![image](https://user-images.githubusercontent.com/98861097/199641629-add93020-67f6-4f3d-be0e-cf4855509ad4.png) <br>
Assigns all face and head groups to the sk_head group; hair and head accessories must still be manually assigned. Also reassigns hand groups; hands must be separated out into separate meshes and exported as separate models to properly function.

(Booby Jiggles version ties each boob to the motion of the thigh by 0.1, will consider making this number adjustable and/or researching other methods in the future)

# Installation
Grab the .zip file from [releases](https://github.com/MFGood/KoikatsuToPES/releases/latest) and navigate to File -> User Preferences:<br>
![image](https://user-images.githubusercontent.com/98861097/199644934-b1497343-be3d-4716-9a0a-dce3c087cb38.png)<br>
Then click "Install Add-on from File..." and select KoikatsuToPES.\<version\>.zip:<br>
![image](https://user-images.githubusercontent.com/98861097/199645002-8f97f628-22f6-4c16-ae79-38e2d27fb657.png)<br>
Navigate to downloads and search "koikatsu" in the top right to find it more easily:
![image](https://user-images.githubusercontent.com/98861097/199645262-fffc5d23-c2f5-40b9-bc67-2f6fad1dfbbe.png)
