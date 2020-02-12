# Change-Darknet-Yolo-Class
Change Darknet Yolo class in file text 

All old class will change to knew one
if you want change all class '1' to class '0'

# Change Class
<pre><code>$ python changeclass.py -i ./imgdir -o 1 -n 0</code></pre>

-i = image/text directory <br/>
-o = old class <br/>
-n = new class <br/>

# Delete Class
<pre><code>$ python changeclass.py -i ./imgdir -d -dc 0</code></pre>

-i = image/text directory <br/>
-d = delete class store True <br/>
-dc = ID class <br/>
