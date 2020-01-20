---
title: What is PSDK ?
date: 2020-01-17
keywords: [PSDK, quick start, standardization, guidance, DJI PSDK]
---
> **NOTE** 
> * This article is **machine-translated**. If you have any questions about this article, please send an <a href="mailto:dev@dji.com">E-mail </a>to DJI, we will correct it in time. DJI appreciates your support and attention.
> * This series of documentation introduces the functions of **PSDK V2.0.0**, as well as the steps and methods of developing payload devices using PSDK V2.0.0. If you are still using PSDK V 1.5.0, please download the documentation of [PSDK V1.5.0](https://terra-1-g.djicdn.com/71a7d383e71a4fb8887a310eb746b47f/psdk/payload-sdk-doc-1.0.zip)

To help developers to develop payload device which is mounted on DJI aircrafts , DJI provides Payload SDK (PSDK), [X-Port standard gimbal](../guide/hardware.html) and [Skyport Adapter Set](../guide/hardware.html). Payload SDK can help developers to obtain adundant **information** from DJI aircrafts, such as power source, communication link and status information.

<div style="text-align: center"> <p> <span><img src="../images/PSDK-features-en.png" width="500" style="vertical-align: middle" alt /> </span></p>
</div>

## Advantages

* **Rich and Complete Features**
Using basic features such as information acquisition, data transmission, and power supply management, and advanced features such as camera, gimbal, payload coordination, and precise positioning, developers could design a **perfect function** payload.

Developers can design full-featured payload devices according to the requirements of  industrial applications.

* **Customized and Scalable**
Besides the DJI Pilot is compatible with payload which is developed using PSDK, DJI provides Mobile SDK to help developers to develop **Mobile Applications** to control the payload; Onboard SDK can help developers to develop control programs to control aircrafts and payload devices to perform tasks automatically. Windows SDK can help developers to develop data processing software and integrate the developed software into a full-featured solution.

* **Support Services**
PSDK not only provides the API and hardware for developing payload devices, but also provides standards, technical support, marketing and cooperation services to help developers develop fully functional aircraft payload equipment and explore the unlimited potential of industrial applications.

## Typical features

* <a href="../camera/camera-initial.html"> <b> Camera Control </b> </a>
* <a href="../tutorial/gimbal-contro.html"> <b> Gimbal Control </b> </a>
* <a href="../tutorial/payload-collaboration.html"> <b> Payoad Collaboration </b> </a>
* <a href="../tutorial/custom-widget.html"> <b> Custom Widget </b> </a>
* <a href="../tutorial/positioning.html"> <b> Positioning </b> </a>
* <a href="../tutorial/data-transmission.html"> <b> Data Communication </b> </a>
* <a href="../tutorial/information-manage.html"> <b> Information Management </b> </a>

## Usage Scenarios

<table id="t1">
  <thead style="text-align:center">
    <tr>
      <td rowspan="2" >Payload</td>
      <td colspan="3">Security</td>
      <td colspan="2">Inspection</td>
      <td colspan="3">Survey</td>
      <td colspan="2">Environment</td>
      <td colspan="2">More Industries</td>
    </tr>
    <tr>
      <td>Public Security</td>
      <td>Fire Fighting	</td>
      <td>Rescue Services	</td>
      <td>Pipeline Inspection</td>
      <td>Factory Inspection</td>
      <td>Geological Survey</td>
      <td>Urban Planning</td>
      <td>Resource</td>
      <td>Ecological Protection</td>
      <td>Biological Protection</td>
      <td>......</td>
    </tr>
  </thead>
  <tbody style="text-align:center">
    <tr>
      <td>Zoom Camera</td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
    </tr>
    <tr>
      <td>Thermal Imaging Camera</td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> - </td>
      <td> - </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
    </tr>
    <tr>
      <td>Infrared Camera</td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> - </td>
      <td> ✓ </td>
      <td> - </td>
      <td> - </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
    </tr>
    <tr>
      <td>Multi-Camera</td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> - </td>
      <td> - </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> - </td>
      <td> - </td>
    </tr>
    <tr>
      <td>Starlight Camera</td>
      <td> ✓ </td>
      <td> - </td>
      <td> ✓ </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
    </tr>
    <tr>
      <td>Lidar</td>
      <td> - </td>
      <td> - </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> - </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
    </tr>
    <tr>
      <td>Gas Detector</td>
      <td> - </td>
      <td> - </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> ✓ </td>
      <td> ✓ </td>
    </tr>
    <tr>
      <td>Radiation Detector</td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> - </td>
    </tr>
    <tr>
      <td>Water Detector</td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> ✓ </td>
      <td> - </td>
    </tr>
    <tr>
      <td>Megaphone</td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
    </tr>
    <tr>
      <td>Searchlight</td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> - </td>
      <td> ✓ </td>
      <td> - </td>
      <td> - </td>
      <td> ✓ </td>
      <td> - </td>
      <td> - </td>
    </tr>
     <tr>
      <td colspan="2" style="border: none;">More Payloads......</td>
    <td style="border: none;text-align:center;"></td>
  </tbody>
</table>

## Using MSDK and OSDK
* MSDK: The Mobile APP developed based on MSDK can control the payload.
* OSDK: The onboard computer could run the control program developed by the developer based on the OSDK.

> **Reference:** [How to use PSDK?](./how-to-use-PSDK.html)
