from game_engine.component import Component


class Collider(Component):

    collider_list = []

    @classmethod
    def add_collider(cls, collider):
        """
        Add a new collider to the collider list
        :param collider: the collider to be added
        """
        cls.collider_list.append(collider)

    @classmethod
    def remove(cls, game_object):
        """
        Remove a collider from the collider list
        :param game_object: the game_object that contains the collider
        """
        if hasattr(game_object, "box_collider"):
            cls.collider_list.remove(game_object.box_collider)
        elif hasattr(game_object, "circle_collider"):
            cls.collider_list.remove(game_object.circle_collider)

    def on_collision(self):
        """
        Check if the have occurred a collision between two colliders
        loop on the collider list to check if this collider have collided with other
        :return: True if collided
        """
        pass

    def __box_collision(self, box):
        """
        Check a collision between this collider and a box_collider
        :param box: the box collider reference
        :return: True if collided
        """
        pass

    def __circle_collision(self, circle):
        """
        Check a collision between this collider and a circle_collider
        :param circle: the circle collider reference
        :return: True if collided
        """
        pass
