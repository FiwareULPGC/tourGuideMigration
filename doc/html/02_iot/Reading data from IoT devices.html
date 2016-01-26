<p style="text-align: justify;">
The first thing you need to do is to connect your IoT devices or Gateways to the above described scenario. This basically means that your IoT devices&rsquo; observations reach a ContextBroker.
</p>

<p style="text-align: justify;">
In the following paragraphs, we provide an example on how you would connect your devices using Ultralight2.0 (UL2.0) - which is a proposed simplification of the SensorML (SML) standard - and get those devices sending &nbsp;their measurements (observations) to the FIWARE Lab public ContextBroker. Ultralight2.0 is selected in this example because of its simplicity.&nbsp;
</p>

<p style="text-align: justify;">
If you want to quickly connect or simulate virtual devices you may also check FIGWAY, a set of simple python scripts working as a client SDK for any desktop PC, laptop or gateway supporting a python2.7 environment. This way you may skip the steps described below and use the python commands as described in the README.md file available at the Github repository linked above.
</p>

<p style="text-align: justify;">
You can find a good summary of the APIs described below also at:<br />
<a href="http://docs.telefonicaiotiotagents.apiary.io/#reference/undefined/device/remove-a-device">http://docs.telefonicaiotiotagents.apiary.io/#reference/undefined/device/remove-a-device&nbsp;</a>
</p>

<p style="text-align: justify;">
Basically, there are four simple steps to follow:
</p>

<p style="text-align: justify;">
<strong>1. Create an IDAS Service</strong><br />
If you are using the public IDAS instance with the public &ldquo;OpenIoT&rdquo; testing service available at 130.206.80.47 (Port 5073) you may skip this step. Just keep in mind the shared secret for this public service (that your devices need to know) is the string &ldquo;4jggokgpepnvsb2uv4s40d59ov&rdquo;.<br />
Otherwise, creating an IDAS Service is basically a simple HTTP POST like this:
</p>

<div class="dev">
<pre class="prettyprint">
<code>POST &lt;idas_host&gt;:&lt;idas_port&gt;/iot/services
//Example: HTTP POST: http://130.206.80.40:5371/iot/services 
Headers: {&#39;content-type&#39;: &#39;application/json&rsquo;; &#39;X-Auth-Token&#39; : [TOKEN]; &quot;Fiware-Service: OpenIoT&rdquo;; &quot;Fiware-ServicePath: /&quot;}
Payload:
{
  &quot;services&quot;: [
    {
    &quot;apikey&quot;: &quot;4jggokgpepnvsb2uv4s40d59ov&quot;,
    &quot;token&quot;: &quot;token2&quot;,
    &quot;cbroker&quot;: &quot;http://0.0.0.0:1026&quot;,
    &quot;entity_type&quot;: &quot;thing&quot;,
    &quot;resource&quot;: &quot;/iot/d&quot;
    }
  ]
}
</code></pre>

<p style="text-align: justify;">
Where 0.0.0.0:1026 might be replaced by a private instance of ContextBroker or just leave it like this (0.0.0.0:1026) if the public instance at the same VM (130.206.80.40:1026) will be used. The apikey string should be updated with a shared secret to be known by devices.
</p>

<p style="text-align: justify;">
<strong>2.&nbsp;&nbsp; &nbsp;Register your IoT device</strong><br />
Before your device sends observations or receives commands a register operation is needed:
</p>
</div>

<div class="dev">
<pre class="prettyprint">
<code>POST &lt;idas_host&gt;:&lt;idas_port&gt;/iot/devices
//Example: http://130.206.80.40:5371/iot/devices 
Headers: {&#39;content-type&#39;: &#39;application/json&rsquo;; &#39;X-Auth-Token&#39; : [TOKEN]; &quot;Fiware-Service: OpenIoT&rdquo;; &quot;Fiware-ServicePath: /&quot;}
Payload:
{&quot;devices&quot;: [
    { &quot;device_id&quot;: &rdquo;[DEV_ID]&quot;,
    &quot;entity_name&quot;: &rdquo;[ENTITY_ID]&quot;,
    &quot;entity_type&quot;: &quot;thing&quot;,
    &quot;timezone&quot;: &rdquo;Europe/Madrid&quot;,
&quot;attributes&quot;: [
        { &quot;object_id&quot;: &quot;t&quot;,
        &quot;name&quot;: &quot;temperature&quot;,
        &quot;type&quot;: &quot;int&quot;
        } ],
 &quot;static_attributes&quot;: [
        { &quot;name&quot;: &quot;att_name&quot;,
        &quot;type&quot;: &quot;string&quot;,
        &quot;value&quot;: &quot;value&quot;
        }]}]}
</code></pre>

<p>
The important parameters to be defined are:<br />
●&nbsp;&nbsp; &nbsp;<span style="color:#0000CD;">[DEV_ID]</span> the device identifier at IDAS.<br />
●&nbsp;&nbsp; &nbsp;<span style="color:#0000CD;">[ENTITY_ID]</span> the entity ID to be used at the ContextBroker will be &ldquo;thing:[ENTITY_ID]&rdquo;<br />
●&nbsp;&nbsp; &nbsp;<span style="color:#0000CD;">&quot;attributes&quot;</span> they should include an alias (a letter representing this attribute).<br />
●&nbsp;&nbsp; &nbsp;<span style="color:#0000CD;">&quot;static_attributes&quot;</span> only if your device needs to define static attributes (sent in every observation)
</p>

<p>
<strong>3. &nbsp; &nbsp; Send Observations related to your IoT device</strong><br />
Sending an observation from IoT devices is extremely efficient and simple with the following query:
</p>
</div>

<div class="dev">
<pre class="prettyprint">
<code>POST  &lt;idas_host&gt;: &lt;idas_port&gt;/d?k= &lt;apikey&gt;&amp;i= &lt;device_ID&gt;
//Example: http://130.206.80.40:5371/iot/d?k=[APIKEY]&amp;i=[DEV_ID]
Headers: {&#39;content-type&#39;: &#39;application/text&rsquo;; &#39;X-Auth-Token&#39; : [TOKEN]; &quot;Fiware-Service: OpenIoT&rdquo;; &quot;Fiware-ServicePath: /&quot;}
Payload: &lsquo; t|25&lsquo;
</code></pre>

<p style="text-align: justify;">
The previous example sends an update of the Temperature attribute that is automatically sent by IDAS to the corresponding entity at the ContextBroker and FIWARE Service defined in our IDAS service.
</p>

<p style="text-align: justify;">
Sending multiple observations in the same message is also possible with the following payload:
</p>
</div>

<div class="dev">
<pre class="prettyprint">
<code>//&ldquo;alias1|value1#alias2|value2#alias3|value3...&rdquo;
//Example: http://130.206.80.40:5371/iot/d?k=[APIKEY]&amp;i=[DEV_ID]
Headers: {&#39;content-type&#39;: &#39;application/text&rsquo;; &#39;X-Auth-Token&#39; : [TOKEN]; &quot;Fiware-Service: OpenIoT&rdquo;; &quot;Fiware-ServicePath: /&quot;}
Payload: &lsquo;t|23#h|80#l|95#m|Quiet&lsquo;
</code></pre>

<p style="text-align: justify;">
<strong>4. &nbsp; &nbsp;&nbsp;Reading measurements sent by your IoT device</strong><br />
Finally, after connecting your IoT devices this way you (or any other developer with the right access permissions) should be able to use the ContextBroker NGSI API to read the NGSI entity assigned to your device.&nbsp;
</p>

<p style="text-align: justify;">
The Entity ID will be the following &ldquo;thing:[ENTITY_ID]&rdquo;.
</p>

<p style="text-align: justify;">
In our particular example described above, you may check in the public ContextBroker (at 130.206.80.40:1026), the Entity_ID=&rdquo;thing:[ENTITY_ID]&rdquo; and the attribute &ldquo;Temperature&rdquo; with the correct updated value. For examples on how to access the ContextBroker, please refer to this component section.
</p>

<p>
&nbsp;
</p>
</div>
