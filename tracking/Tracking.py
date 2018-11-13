from threading import Thread
import time
import cv2
import numpy as np
from tracking.trackableobject import TrackableObject
from tracking.centroidtracker import CentroidTracker


class Tracking(Thread):
    def __init__(self):
        self.trackableObjects = {}
        self.totalUp = 0
        self.totalDown = 0
        self.rects = [] # list of bounding box rectangles returned by either (1) our object detector or (2) the correlation trackers

    def tracking(self, frame):
        ct = CentroidTracker(maxDisappeared=10, maxDistance=30)

        # use the centroid tracker to associate the (1) old object
        # centroids with (2) the newly computed object centroids
        objects = ct.update(self.rects)


        for (objectID, centroid) in objects.items():
            # check to see if a trackable object exists for the current
            # object ID
            to = self.trackableObjects.get(objectID, None)
            # print("ID: " + str(objectID) + " cX, cY: " + str(centroid))
            # if there is no existing trackable object, create one
            if to is None:
                to = TrackableObject(objectID, centroid)

            # otherwise, there is a trackable object so we can utilize it
            # to determine direction
            else:
                # the difference between the y-coordinate of the *current*
                # centroid and the mean of *previous* centroids will tell
                # us in which direction the object is moving (negative for
                # 'up' and positive for 'down')
                y = [c[1] for c in to.centroids]
                print(y)
                direction = centroid[1] - np.mean(y)

                # print(str(np.mean(x)))
                # print("direction: " +  str(direction) + " centroid: " + str(centroid[0]))
                # print("dir: " +  str(direction) + "centroid:" + str(centroid[0]) + ", " + str(centroid[1]))

                to.centroids.append(centroid)

                # check to see if the object has been counted or not
                if not to.counted:
                    # if the direction is negative (indicating the object
                    # is moving up) AND the centroid is above the center
                    # line, count the object
                    if direction < 0 and y[0] >= 240 and y[-1] <= 240:
                        self.totalUp += 1
                        to.counted = True

                    # if the direction is positive (indicating the object
                    # is moving down) AND the centroid is below the
                    # center line, count the object
                    elif direction > 0 and y[0] <= 240 and y[-1] >= 240:
                        self.totalDown += 1
                        to.counted = True

            # store the trackable object in our dictionary
            self.trackableObjects[objectID] = to

            # отображение центроида объекта
            cv2.circle(frame, (centroid[0], centroid[1]), 6, (255, 255, 255), -1)

            # ID объекта
            text = "ID {}".format(objectID)
            cv2.putText(frame, text, (centroid[0] - 10, centroid[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (255, 255, 255), 2)
