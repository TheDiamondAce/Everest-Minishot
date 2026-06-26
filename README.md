# Everest-Minishot

<img width="1305" height="2000" alt="Everest Minishot Zine With Fallout Requirements" src="https://github.com/user-attachments/assets/1953af01-49ae-4195-89d3-662e532a63cb" />


# Motivation
I wanted to make a camera that was accesible and very good quality, everywhere you go without making it too much of a hassle to take a picture in, whether it be in nature, in rain, in the bustling cities, or in a secluded area. Anywhere, anytime, without any friction to composition.

# What it is
This project is a camera that will be able to be hung on your keychain, being able to take videos and picture without friction, from turning it on to getting the composition like how you see it. It will be similar to that of the dji nano. And will be GREAT! alr probably gonna change that later lmao

# How to build

To build, you will need to get the chassis by 3D printing it, order the PCB as in the Repo, buy a raspberry pi zero 2 W, and also get the battery as shown in the B.O.M, then to build, you will need to screw in the components in the enclourse. Then after, you will need to follow the wiring diagram as shown in the PCB files, connected the buttons as shown in the PCB wiring respectively. For the Display you will need to connect the SDA to GPIO 27 and SDL to GPIO 22, since the sda and scl native ports on the raspeberry pi is being occupied by the buttons, you will then need to drag everything in the code file and put it to the root of the raspberry pi so that it runs on startup. Then after you will have to get the code from the code file and flash it to the raspberry pi

# BOM
| Name | Description | Total (USD) | Quantity | Why | Link |
| --- | --- | --- | --- | --- | --- |
| 12mm Button | A tactile switch that either connects a cirucuit or disconnects depending on input | $8.12 | 2 | So you can click stuff to memorize for the minigame | https://www.amazon.com/Uxcell-a11111400ux0132-Momentary-Tactile-Button/dp/B0090VQLDK |
| SH 1107 OLED | Display used to show camera input and modes | $12.39 | 1 | To see what inputs to do next and other data | https://www.amazon.com/ACEIRMC-ILI9341-Display-Touch-240X320/dp/B0C4D5S6G5/ref=sr_1_10_sspa?crid=1KKGFFL8GGC72&dib=eyJ2IjoiMSJ9.aNbS-hCnwROiq-lihDWLj0bSTkExzZcUEg9Thz-MRRtS2XSDTZusdgq0aD1F0WmFP2z1icua7XtMO6m0dMOpn8SqrOFp1HIlcN4kiqw6-RlV7hZO4ruwCns7e_xrwwarWxaiSyrChwiIRUrUY_RlX9OKgmKKALx-gO4lSBbiMaZfKv6a7KsmvzFghX94ueB0tjP9qSX40MXT01v37X8MMYSJqIt6UnkreQ59ftwFdiegDUDVujNbTPq7P3rk02P9OOVeiCEMzoFH8qXlYbO1NNMZsi5VeRhwTNT7sHwGj98.L9Ilfuyvs66CsTIbDNYf3OsazpswS6k4iaS05y2B6dk&dib_tag=se&keywords=ili9341&qid=1781262418&s=electronics&sprefix=ili%2Celectronics%2C409&sr=1-10-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9tdGY&psc=1 |
| Arduino Zero 2 W | The Microcontroller that will control all functions of the minigame as well as logic. | $15.00 | 1 | To control the whole camera and logic | https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/ |
| Dupont Female-Female Wires | Used to connect modules to microcontroller and circuits. | $6.98 | 5 | Bruh, so the whole thing can get some electricity. | https://www.amazon.com/California-JOS-Breadboard-Optional-Multicolored/dp/B0BRTKTV64?th=1 |
| 3D Printer Enclousure. | The host for all modules necessary in the build |  | 1 | To put all of the modules into one area | can print through hackclub or by yourself with step file |
| Sony IMX576 24MP Camera | A module that uses photons to create an image (a camera) | ~$18.50** | 1 | So the camera becomes a camera | https://sincerefirst.en.made-in-china.com/product/BANRFcJrLdWv/China-24MP-Sony-Imx576-Image-Sensor-Autofocus-Lens-24-Pin-Camera-Module-Smartphone.html |
| Ribbon Flex Extension Cables for Pi Zero&W | A 15mm to 22mm ribbion cable | $8.99 | 1 | So the IMX576 can connect to the Rasberry Pi Zero 2W | https://www.amazon.com/Arducam-Raspberry-Camera-Ribbon-Extension/dp/B085RW9K13/?_encoding=UTF8&pd_rd_w=x8UbO&content-id=amzn1.sym.a9c4acee-9ca0-46be-bae3-532a2b4b0d29%3Aamzn1.symc.5a16118f-86f0-44cd-8e3e-6c5f82df43d0&pf_rd_p=a9c4acee-9ca0-46be-bae3-532a2b4b0d29&pf_rd_r=9X4HZN75VZ4YB08QZNPW&pd_rd_wg=kdRp2&pd_rd_r=617b9bf0-440a-42f2-9107-20efd28b610a&ref_=pd_hp_d_atf_ci_mcx_mr_ |
| USB C connector | A module in which a usb C port is included | $7.49 | 1 | For easy connectivity for the camera for data and power. | https://www.amazon.com/Teansic-Connector-Breakout-Converter-Transfer/dp/B0B4J5NJ2Y/ref=sr_1_3?crid=3IMY4LTK8CFVK&dib=eyJ2IjoiMSJ9._TAav2gmYgzR2fvtTjBYdAncdrRe2JEXz48orUvk4PvnixvgSd7BiMozddiG7ZqMbsxeniI0Ob2XsravI7RVDWU9wPSSekozCTOZsiTwrHoj6EjdCvLMxAoIVEarxsqKP2s8pnMNgndUzJS0R_ih4MMafPWaCmU0tkK2XNSFuRgQQ34bmeG-38jUrw3OvX0DvpUaffIyZVBVBOiWMfQ7aq90x1VNnlj6ZZpW5zrZNUPzYi4rJBfmeRi_U5-NS81sxeag735exzMIqGvhppiLU2VINXloYt8rCbBx6tvqG2A.UchCu6BU6WBTt3usZwzm49mGplQKhnHKdiVavSk4A58&dib_tag=se&keywords=usb%2Bc%2Bconnector%2Bmodule&qid=1781853104&s=industrial&sprefix=usb%2Bc%2Bconnector%2Bmod%2Cindustrial%2C388&sr=1-3&th=1 |
| JST Male Header | A module that allows for female JST wires to connect | $0.04 | 2 | For Carrier PCB connection to Raspberry PI 2W | https://www.taydaelectronics.com/3-pins-jst-xh-2-54-male-connector-straight-180-degree.html |
| Female to Female JST XH 3pin | A module in which connects to the male headers pins | $1.80 | 1 | ~~~~ | https://www.pololu.com/product/5513 |
| JST XH Female to Dupont 4Pin | A cable that has a 4 pin JST XH connector that splits into dupont cables | $0.40 | 1 | To connect the oled display to the raspeberry pi | https://grobotronics.com/jumper-wire-jst-xh-to-separate-dupont.html?variation_id=17936 |
| PCB | A electrical component custom made for a specific task | $30.71 | 1 | For the buttons up top to connect to the rasberry PI Zero. | https://www.pcbway.com/orderonline.aspx?outsideid=b538974d-ef2e-4f84-a5e9-d126d94cb61b |
| THE LINKS USED MIGHT HAVE MULTIPLE PIECES SINCE THEY ARE THE BEST BANG FOR BUCK ON AMAZON.*** |  |  |  |  |  |
|  | MIGHT BE ABLE TO ASK FOR A SAMPLE PIECE, OTHERWISE ITS 92.5** |  |  |  |  |
|  | TOTAL = | $91.92 |  |  |  |


# CAD

## Isometric
<img width="814" height="796" alt="image" src="https://github.com/user-attachments/assets/d0e5430c-cd1d-481f-958d-9bce1c191176" />

## Front
<img width="814" height="796" alt="image" src="https://github.com/user-attachments/assets/50796923-7698-4068-93f0-d54bdd632a9e" />

## Side

<img width="814" height="796" alt="image" src="https://github.com/user-attachments/assets/df33648b-588b-49e3-8700-98343b395e15" />

## Back

<img width="814" height="796" alt="image" src="https://github.com/user-attachments/assets/eb7dab63-4277-4d20-a2b6-84e581787781" />

# Wiring Diagram/PCB
<img width="1008" height="746" alt="image" src="https://github.com/user-attachments/assets/2d54d394-a7dd-4f64-bcb9-a1ba5c60b2cf" />
(The 01x03 jst connecter will be connected to the GPIO 3 and GPIO 4 pins as well as GND pin respectively)

# Photo Taken of Live Viewfinder for the Camera (Everest Minishot Simulator)
<img width="260" height="160" alt="img_20260620-153809" src="https://github.com/user-attachments/assets/e16f40c0-bea5-4770-89f7-ff0cb8364cda" />




