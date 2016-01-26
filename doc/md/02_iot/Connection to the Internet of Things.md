<p style="text-align: justify;">
Connecting &ldquo;objects&rdquo; or &ldquo;things&rdquo; involves the need to overcome a set of problems arising in the different layers of the communication model. Using its data or acting upon them requires interaction with a heterogeneous environment of devices running different protocols (due to the lack of globally accepted standards), dispersed and accessible through multiple wireless technologies. &nbsp;
</p>

<p style="text-align: justify;">
Devices have a lot of particularities so it is not feasible to provide a solution where one size fits all. They are resource constrained and can&rsquo;t use full standard protocol stacks: they cannot transmit information too frequently due to battery drainage, they are not always reachable since they are connected through heterogeneous wireless networks, their communication protocols are too specific and lack integrated approach, and they use different data encoding languages, so it is tricky to find a global deployment. &nbsp;
</p>

<p style="text-align: justify;">
There are three IoT typical use-case scenarios (combination of IoT GEs) described in the <a href="http://forge.fiware.org/plugins/mediawiki/wiki/fiware/index.php/Internet_of_Things_%28IoT%29_Services_Enablement_Architecture">FIWARE IoT architecture</a>. The simplest and more tested one is called &ldquo;Common Simple Scenario&rdquo; and it is depicted in the following picture:&nbsp;
</p>

<p>
<a href="http://www.fiware.org/wp-content/uploads/2014/11/3.png"><img alt="3" class="aligncenter size-full wp-image-37954" height="260" src="http://www.fiware.org/wp-content/uploads/2014/11/3.png" width="508" /></a>
</p>

<p style="text-align: center;">
<strong>FIWARE IoT Device Management GE architecture</strong>
</p>

<p style="text-align: justify;">
This simple scenario considers only two Generic Enablers implementations:
</p>

<ul>
<li style="text-align: justify;">
<strong>Orion ContextBroker:</strong> That remains as the main front-end for developers. Developers access IoT data as attributes of entities representing devices and Developers may also send commands to devices by updating command-related attributes, providing they have access rights for that operation.
</li>
<li style="text-align: justify;">
<strong>IDAS Backend Device Manager:</strong> This component stays at the southbound of the Orion ContextBroker and it is used by IoT integrators to connect devices in this scenario.
</li>
</ul>

<p style="text-align: justify;">
IDAS supports several IoT protocols with a modular architecture where modules are called &ldquo;IoT Agents&rdquo;. Therefore, integrators need to determine first which protocol they will be using to connect devices and select the right IoT Agent.&nbsp;<br />
At present, the following IoT Agents and supported IoT protocols are:
</p>

<ul>
<li style="text-align: justify;">
<strong>IDAS Ultralight2.0 &amp; MQTT:</strong> Supports Ultralight2.0/HTTP and/or MQTT (depends on the compilation options). Github repository is <a href="https://github.com/telefonicaid/fiware-IoTAgent-Cplusplus/">here</a>. FIWARE Lab public instance details are <a href="http://catalogue.fiware.org/enablers/backend-device-management-idas/instances">here</a>.&nbsp;
</li>
<li style="text-align: justify;">
<strong>IDAS LWM2M:</strong> Supports OMA LightweightM2M over IETF CoAP (IPv4 and IPv6 supported). Github repository is <a href="https://github.com/telefonicaid/lightweightm2m-iotagent">here</a>. FIWARE Lab public instance details are <a href="http://catalogue.fiware.org/enablers/backend-device-management-idas/instances">here</a>.
</li>
</ul>

<p style="text-align: justify;">
For simplicity, in this article Ultralight2.0/HTTP is explained. Please refer to the FIWARE Catalogue to find out more information on the other options.<br />
If you are interested to connect your application to the Internet of Things, keep on reading:
</p>

<ul>
<li>
<a href="http://www.fiware.org/devguides/connection-to-the-internet-of-things/how-to-read-measures-captured-from-iot-devices/">How to read measures captured from IoT devices</a>&nbsp;
</li>
<li>
<a href="http://www.fiware.org/devguides/connection-to-the-internet-of-things/how-to-act-upon-iot-devices/">How to act upon IoT devices</a>
</li>
</ul>

<p>
&nbsp;
</p>
