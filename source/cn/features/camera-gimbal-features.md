---
title: Payload SDK Features - Camera/Gimbal Interfaces
date: 2018-03-28
keywords: [introduction, overview, Payload SDK]
---

## Camera and Gimbal Payload Interface Support
Payload SDK provides support for camera and gimbal payloads that will allow your payload to function seamlessly with DJI Mobile SDK and DJI Pilot.  DJI Pilot provides UI for camera and gimble payloads, and Mobile SDK provides the corresponding interface for camera and gimbal payloads. This support is intended to be used in the following manner:

- Payload SDK provides interfaces that are interpreted by the aircraft/MSDK in the same manner as native DJI payloads.
- It is the developer's responsibility to implement these features as defined by the interface.
- For example, the PSDK provides a Zoom API. This means that this function will be called when a MSDK application calls the Zoom API on the mobile side or zoom button press on DJI Pilot. It is up to you, as a developer, to implement the zoom functionality for your own payload such that when the zoom function is invoked, your payload physically executes the zoom.

### Camera Interface Support

<table id="t01">
  <thead>
    <tr>
      <th>Interface features</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Camera working modes</th>
      <td>Capture mode and recording mode.</td>        
    </tr>
    <tr>
      <td>Capture modes</th>
      <td>Single capture, continuous capture, and interval capture.</td>        
    </tr>
    <tr>
      <td>Recording modes</th>
      <td>Start recording and stop recording.</td>        
    </tr>
    <tr>
      <td>SD function</th>
      <td>Obtain SD card status and format SD card.</td>        
    </tr>
    <tr>
      <td>Metering function</th>
      <td>Metering modes: center-weighted metering, average metering, spot metering. The spot metering supports set spot metering areas.</td>        
    </tr>
    <tr>
      <td>Focus function</th>
      <td>Support to set the autofocus focus area.</td>        
    </tr>
    <tr>
      <td>Zoom function</th>
      <td>Support for fixed speed zoom and position zoom.</td>        
    </tr>
  </tbody>
</table>

### Gimbal Interface Support

<table id="t01">
  <thead>
    <tr>
      <th>Interface features</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Gimbal speed control</th>
      <td>Set the gimbal's angular velocity.</td>        
    </tr>
    <tr>
      <td>Gimbal return to center</th>
      <td>Gimbal return to center to keep the same direction with the aircraft nose.</td>        
    </tr>
    <tr>
      <td>Gimbal mode settings</th>
      <td>Obtain the current gimbal attitude and rotate limit.</td>        
    </tr>
  </tbody>
</table>
