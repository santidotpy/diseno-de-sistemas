

# composite pattern

class Component(object):
    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass

class Child(Component): # inherits from the abstract class, Component
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        # this is where we store the name of your child item!
        self.name = args[0]

    def component_function(self):
        # print the name of your child item here!
        print("{}".format(self.name))

class Composite(Component): # inherits from the abstract class, Component
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs) # call the init method of the abstract object, Component

        # this is where we store the name of the composite object
        self.name = args[0]

        # this is where we keep our child items
        self.children = []

    def append_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def component_function(self):
            
            # print the name of the composite object
            print("{}".format(self.name))
    
            # iterate through the child objects and invoke their component function printing their names
            for i in self.children:
                i.component_function()

# build a composite submenu 1
sub1 = Composite("submenu1")

# create a new child sub_submenu 11
sub11 = Child("sub_submenu 11")
# create a new child sub_submenu 12
sub12 = Child("sub_submenu 12")

# add the sub_submenu 11 to submenu 1
sub1.append_child(sub11)
# add the sub_submenu 12 to submenu 1
sub1.append_child(sub12)

sub1.component_function()
# build a top-level composite menu
top = Composite("top_menu")

# build a submenu 2 that is not a composite
sub2 = Child("submenu2")

# add the composite submenu 1 to the top-level composite menu
top.append_child(sub1)

# add the plain submenu 2 to the top-level composite menu
top.append_child(sub2)

# let's test if our Composite pattern works!
top.component_function()

