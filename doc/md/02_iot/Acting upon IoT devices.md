<p>
In order to send commands to devices, developers just need to know which attributes correspond to commands and update them.
</p>

<p>
IoT integrators need to declare the command related attributes at the registry process (POST request) in the following way:
</p>

<div class="dev">
<pre class="prettyprint">
<code>POST &lt;idas_host&gt;:&lt;idas_port&gt;/iot/devices
//Example: HTTP POST: http://130.206.80.40:5371/iot/devices 
Headers: {&#39;content-type&#39;: &#39;application/json&rsquo;; &#39;X-Auth-Token&#39; : [TOKEN]; &quot;Fiware-Service: OpenIoT&rdquo;; &quot;Fiware-ServicePath: /&quot;}
Payload:
{&quot;devices&quot;: [
    { &quot;device_id&quot;: &rdquo;[DEV_ID]&quot;,
    &quot;entity_name&quot;: &rdquo;[ENTITY_ID]&quot;,
    &quot;entity_type&quot;: &quot;thing&quot;,
    &quot;endpoint&quot;: &quot;http://[DEVICE_IP]:[PORT]&quot;,
    &quot;timezone&quot;: &rdquo;Europe/Madrid&quot;,
    &quot;commands&quot;: [
        { &quot;name&quot;: &rdquo;RawCommand&quot;,
        &quot;type&quot;: &quot;command&quot;,
        &quot;value&quot;: &ldquo;[Dev_ID]@RawCommand|%s&quot;
        } ],
    &quot;attributes&quot;: [
</code></pre>

<p>
&nbsp;
</p>

<p style="text-align: justify;">
Any update on this attribute &ldquo;RawCommand&rdquo; at the NGSI entity in the ContextBroker will send a command to your device.
</p>

<p style="text-align: justify;">
If the row <span style="color:#FF0000;"><strong>&quot;endpoint&quot;: &quot;</strong></span><strong><span style="color:#0000FF;">http://[DEVICE_IP]:[PORT</span><span style="color:#FF0000;">]&quot;</span></strong> is declared, then your device is supposed to be listening for commands at that URL in a synchronous way.
</p>

<p style="text-align: justify;">
If that enpoint is not declared (if that row does not exist) then yur devices is supposed to work in a polling mode and therefore receiving commands in an asynchronous way (i.e. when the device proactively asks for commands).
</p>

<p style="text-align: justify;">
For a device working in the polling mode to receive commands, the full pending queue of commands will be received with the following HTTP GET request:
</p>

<p>
&nbsp;
</p>
</div>

<div class="dev">
<pre class="prettyprint">
<code>POST &lt;idas_host&gt;:&lt;idas_port&gt;/d?k=&lt;apikey&gt;&amp;i=&lt;device_ID&gt;
//Example: HTTP GET:
Headers: {&#39;content-type&#39;: &#39;application/text&rsquo;; &#39;X-Auth-Token&#39; : [TOKEN]; &quot;Fiware-Service: OpenIoT&rdquo;; &quot;Fiware-ServicePath: /&quot;}
http://130.206.80.40:5371/iot/d?k=[APIKEY]&amp;i=[DEV_ID]
</code></pre>
</div>
