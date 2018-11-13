### PEOPLE COUNTER

This is investigation prototype of application, which main goal is to count number of people that enter and leave some area

Started 28.08.2018

### Local setup
*Create a local virtual python environment*
```bash
pip3 install virtualenv

virtualenv -p python3 python-env

source python-env/bin/activate
```

*Install the dependencies for the project*

```bash
pip install -r requirements.txt
```

**For windows anaconda can be used to ease installation**

### Project tree
```
.
├── classes.py
├── people_counter.py                       people counting algorithm
├── pl.py                                   statistic visualisation
├── streaming                               streaming ivestigation
│   ├── Stream.py
│   ├── ffserver.py
├── tracking                                centroid tracking algorithm
│   ├── centroidtracker.py
│   ├── trackableobject.py
│   └── Tracking.py
├── README.md   
├── mobilenet_ssd                           Caffe deep learning model files
│   ├── MobileNetSSD_deploy.caffemodel
│   └── MobileNetSSD_deploy.prototxt             
├── requirements.txt                        dependencies
└── start.py                                app entry point
```

### Briefly about the algorithm
- get frame
    - every *n* frame:
        - convert the frame to a blob and pass the blob through the network and obtain the detections
        - loop over detections and filter out weak and useless detections
        - construct a dlib rectangle object and then start the dlib correlation tracker. Add the tracker to our list of trackers
    - else:
        - update the tracker and grab the updated position
        - use the centroid tracker to associate the (1) old object centroids with (2) the newly computed object centroids
    - loop over the tracked objects:
        - check to see if a trackable object exists for the current object ID. Create if there is no existing trackable object
        - otherwise determine utilize it to determine direction and count 
    - draw
### HOW TO

```bash
 python start.py
```

