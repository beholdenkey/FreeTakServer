#######################################################
# 
# Event.py
# Python implementation of the Class Event
# Generated by Enterprise Architect
# Created on:      10-Feb-2020 3:58:29 PM
# Original author: Giu Platania
# 
#######################################################
from TAKfreeServer.Model.point import point
from TAKfreeServer.Model.detail import detail

class Event:
    """represent a TAK event: this class is instantiated with a standard set of values.
    """
    m_point = "point()"
    m_detail = "detail()"
    # Gives a hint about how the coordinates were generated
    how = "m-g"
    # Schema version of this event instance (e.g. 2.0)
    version = "2.0"
    # time stamp: when the event was generated
    time = "%Y-%m-%dT%H:%M:%SZ"
    # <font color="#008000">Hierarchically organized hint about event type</font>
    type = "a-h-G-E-V"
    # ending time when an event should no longer be considered valid
    stale = "%Y-%m-%dT%H:%M:%SZ"
    # Globally unique name for this information on this event
    uid = "UIDString"
    # starting time when an event  should be considered valid
    Start = "%Y-%m-%dT%H:%M:%SZ"