# g-noobradio-sna

My diletantic first try at making something that should work a bit like a scalar network analyzer, using a hackrf and a rtlsdr.
Please, don't ask me about that constant source, i followed a video on youtube, i'm just happy the sweep is working.
Mainly uploading this just to have a backup somewhere, and in case somebody finds this interesting and maybe wants to help. 


All the tests for now with a Pi attenuator where all 3 resistors are 100 Ohm, which is probably not ideal, but 100 Ohm resistors are easier to get than seventy-odd Ohm non standard resistors. Seems to work ok:

![image](https://user-images.githubusercontent.com/36307725/147415303-791a9968-f479-4664-9d06-b6d3b8623760.png)

How To Use The Flowgraph:

Disclaimer: This seems to work on my box, if you break your rtlsdr or hackrf, please don't blame me! 

Adjust the output file name and path.
Maybe check if the settings are ok for your setup. 
Run it. It will stop recording after one sweep, but will start the sweep again at F1, so you'd need to stop the flowgraph manually.
Or just keep staring at the time sink, that's ok.
Change the output file name, then run it again.

Once finished, go to https://wiki.gnuradio.org/index.php/Octave and follow the instructions there.

Then in ocatve, first maybe tell it to use gnuplot:
graphics_toolkit("gnuplot")

then read and plot the data:

cal1=read_float_binary('cal1');
plot(cal1);


maybe join some of them into one array: 

cal2=read_float_binary('cal2');
cal2=read_float_binary('cal3');
cal4=read_float_binary('cal4');

cal_all=[cal1,cal2,cal3,cal4];
plot(cal_all);

see adorable squiggly lines: 


![image](https://user-images.githubusercontent.com/36307725/147416651-2fcc676b-f7aa-4d1d-817c-f81fccfdfc1b.png)
