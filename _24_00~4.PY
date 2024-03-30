
class Profile:
    def __init__(self, name):
        self.name = name
        self.has_beef_with_Javascript = False

def can_learn_javascript_decorator(function):
    def wrapper_function(*args, **kwargs):
        if args[1].has_beef_with_Javascript == False:
            return function(args[0], args[1])
        else:
            print(f"{args[1].name} cannot start learning JavaScript due to existing beef with it.")
    return wrapper_function      # removed () from the end of the function name.


@can_learn_javascript_decorator
def start_learning_javascript(none, profile):
    print(f"This is {profile.name}'s new JavaScript lesson.")

new_profile = Profile("Jeremy")
new_profile.has_beef_with_Javascript = False
start_learning_javascript(None, new_profile)




#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in == False:   # user.is_logged_in == True:   we were only able to pass in the FUNCTION itself,
#             function(args[0])
#     return wrapper
#
# @is_authenticated_decorator
# def create_blog_post(user):
#     print(f"This is {user.name}'s new blog post.")
#
# new_user = User("Thomas")
# new_user.is_logged_in = True
# create_blog_post(new_user)