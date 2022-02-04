## Sri Lanka Covid-19 Dashboard

Just another covid-19 dashboard that displays covid-19 information of sri lanka.

- Test the deployement [Click Here](http://covid.hirusha.xyz)
- Additional Information: [Click Here](https://hirusha-adi.github.io/Sri-Lanka-Covid-19-Dashboard/) 

## Images

![image](https://user-images.githubusercontent.com/36286877/152511550-18ce631a-ed09-4319-bdb2-882b5adc4728.png)

![image](https://user-images.githubusercontent.com/36286877/152511564-47346d36-815b-434d-a7bd-911eeedac741.png)

## Available Routes

<table>
<thead>
  <tr>
    <th>Route</th>
    <th>Information</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>/</td>
    <td>Home Page. Everything important is displayed simply</td>
  </tr>
  <tr>
    <td>/more</td>
    <td>Additional Information (Daily PCR and Antigen Testing Data)</td>
  </tr>
  <tr>
    <td>/more/pcr</td>
    <td>Additional Information (Display all PCR Testing Data available)</td>
  </tr>
  <tr>
    <td>/more/antigen</td>
    <td>Additional Information (Display all Antigen Testing Data available)</td>
  </tr>
</tbody>
</table>

## Installing the Web Server

### Arch Linux

run the commands below, line by line

```bash
sudo pacman -Syyuu --noconfirm
sudo pacman -S git python python-pip --noconfirm
cd ~
git clone https://github.com/hirusha-adi/Sri-Lanka-Covid-19-Dashboard.git
cd Sri-Lanka-Covid-19-Dashboard
pip3 install -r requirements.txt
python3 covid.py # to start the web app
# CTRL + Z
# bg
# disown -h
```
### Ubuntu/Debian

run the commands below, line by line

```bash
sudo apt install && sudo apt upgrade -y
sudo apt install git python3 python3-pip -y
cd ~
git clone https://github.com/hirusha-adi/Sri-Lanka-Covid-19-Dashboard.git
cd Sri-Lanka-Covid-19-Dashboard
pip3 install -r requirements.txt
python3 covid.py # to start the web app
# CTRL + Z
# bg
# disown -h
```

### Windows

1. Download and install Python3. Make sure to 'Add to PATH' when install python3

![image1](https://www.tutorials24x7.com/uploads/2019-12-26/files/3-tutorials24x7-python-windows-install.png)

2. Download the code as a .zip file from this Github Reposotory

![image2](https://cdn.discordapp.com/attachments/935515175073763398/937186561299197952/unknown.png)

(this above image might not be the same)

3. Extract the downloaded `.zip` file
4. open `cmd` in that folder
5. run `pip install -r requirements.txt`
6. run `python covid.py` to start the web app






