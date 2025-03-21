import math

from RoadwayGeometry.Angles import DirectionAngle
from RoadwayGeometry.Horizontal.curve_direction import CurveDirection
from BridgeMath.num_compare import effectively_equal


class CircularHorizontalCurve:
    '''
    Circular Horizontal Curve class that represents a horizontal curve in a roadway
    :param pi_sta: PI station
    :param angle_in: Angle of the curve at the beginning
    :param angle_out: Angle of the curve at the end
    :param degree_of_curvature: Degree
    
    '''
    def __init__(self, pi_sta: float, angle_in: DirectionAngle, angle_out: DirectionAngle,
                 degree_of_curvature: float):
        self.pi_station = pi_sta
        self.angle_in = angle_in
        self.angle_out = angle_out
        self.degree_of_curvature = degree_of_curvature
        self._interior_angle = self.__calculate_interior_angle()

    @property
    def radius(self):
        """
        Curve radius
        :return: Curve radius
        """
        return 100.0 / self.degree_of_curvature

    @property
    def direction(self) -> CurveDirection:
        delta = self.angle_out - self.angle_in

        if delta.angle > math.pi:  # curve right
            return CurveDirection.RIGHT
        else:  # curve left
            return CurveDirection.LEFT

    @property
    def interior_angle(self):
        """
        Sweep angle of curve
        :return: Interior angle (radians)
        """
        return self._interior_angle

    @property
    def length(self):
        """
        Length of the horizontal curve
        :return: Length
        """
        return self.radius * self._interior_angle

    @property
    def pc_station(self):
        """
        Beginning of the horizontal curve station
        :return: PC Station
        """
        return self.pi_station - self.tangent_distance

    @property
    def pt_station(self):
        """
        End of the horizontal curve station
        :return: PT Station
        """
        return self.pc_station + self.length

    @property
    def tangent_distance(self):
        """
        Tangent distance from either PC or PT to the PI
        :return: Tangent distance
        """
        return self.radius * math.tan(self._interior_angle / 2.0)

    def on_curve(self, station) -> bool:
        """
        Checks if a given station is on the horizontal curve
        :param station: Station to check
        :return: true if station is on curve; false otherwise
        """
        return self.pc_station <= station <= self.pt_station

    def __calculate_interior_angle(self) -> float:
        angle_out = self.angle_out.angle if self.angle_out.angle <= math.pi else self.angle_out.angle - 2 * math.pi
        angle_in = self.angle_in.angle if self.angle_in.angle <= math.pi else self.angle_in.angle - 2 * math.pi

        return math.fabs(angle_out - angle_in)

    def __eq__(self, other: 'CircularHorizontalCurve'):
        return effectively_equal(self.pi_station, other.pi_station) and \
               effectively_equal(self.interior_angle, other.interior_angle)
