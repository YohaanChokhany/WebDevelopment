import web
import os
from pymongo import MongoClient
import string
from Models import GetAnswersModel

web.config.debug = False

urls = (
    "/", "Home",
    "/yohaan-chokhany", "YohaanChokhany",
    "/about-us", "AboutUs",
    "/bday-countdown", "BdayCountdown",
    "/punch-a-moose", "Moose",
    "/not-found", "NotFound",
    "/try-it-yourself", "TryItYourself",
    "/class1", "Class1",
    "/class2", "Class2",
    "/class3", "Class3",
    "/class4", "Class4",
    "/todo", "ToDo",
    "/search-engine", "SearchEngine",
    "/random-past-paper", "RandomPastPaper",
    "/choose-past-paper", "ChoosePastPaper",
    "/next-class", "NextClass",
    "/textarea-autofocus-attribute", "TextareaAutofocusAttribute",
    "/button-autofocus-attribute", "ButtonAutofocusAttribute",
    "/input-autofocus-attribute", "InputAutofocusAttribute",
    "/youtube", "YouTube",
    "/css-buttons", "CSSButtons",
    "/trial", "Trial",
    "/encryption", "Encryption",
    "/calculator", "Calculator",
    "/codepen", "CodePen",
    "/mcq", "MCQ",
    "/get-mcq-answers", "GetAnswers",
    '/(.*)/', 'Redirect',
    "/(.*)", "GoToNotFound",
)
app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={'user': None})
session_data = session._initializer

render = web.template.render("Views/Templates", base="MainLayout", globals={'session': session_data,
                                                                            'current_user': session_data["user"]})


# Classes/routes


class YohaanChokhany:
    def GET(self):
        return render.YohaanChokhany()


class YouTube:
    def GET(self):
        return render.YouTube()


class MCQ:
    def GET(self):
        return render.MCQ()


class AboutUs:
    def GET(self):
        return render.AboutUs()


class BdayCountdown:
    def GET(self):
        return render.BdayCountdown()


class Class1:
    def GET(self):
        return render.Class1()


class Class2:
    def GET(self):
        return render.Class2()


class Class3:
    def GET(self):
        return render.Class3()


class Class4:
    def GET(self):
        return render.Class4()


class SearchEngine:
    def GET(self):
        return render.SearchEngine()


class RandomPastPaper:
    def GET(self):
        return render.RandomPastPaper()


class ChoosePastPaper:
    def GET(self):
        return render.ChoosePastPaper()


class NextClass:
    def GET(self):
        i = 0
        running = True
        while running:
            i += 1
            if not os.path.exists("Views/Templates/Class" + str(i) + ".html"):
                i -= 1
                break
        web.seeother("/class" + str(i))


class TextareaAutofocusAttribute:
    def GET(self):
        return render.TextareaAutofocusAttribute()


class ButtonAutofocusAttribute:
    def GET(self):
        return render.ButtonAutofocusAttribute()


class InputAutofocusAttribute:
    def GET(self):
        return render.InputAutofocusAttribute()


class TryItYourself:
    def GET(self):
        return render.TryItYourself()


class Redirect:
    def GET(self, path):
        web.seeother("/" + path)


class GoToNotFound:
    def GET(self, path):
        web.seeother("/not-found")


class Home:
    def GET(self):
        return render.Home()


class Moose:
    def GET(self):
        return render.Moose()


class NotFound:
    def GET(self):
        return render.NotFound()


class CSSButtons:
    def GET(self):
        return render.CSSButtons()


class Trial:
    def GET(self):
        return render.Trial()


class Encryption:
    def GET(self):
        return render.Encryption()


class Calculator:
    def GET(self):
        return render.Calculator()


class CodePen:
    def GET(self):
        return render.CodePen()


class GetAnswers:
    def POST(self):
        data = web.input()
        get_answers_model = GetAnswersModel.GetAnswersModel()
        answers = get_answers_model.get_answers(data)
        return answers


class ToDo:
    def GET(self):
        return render.ToDoList()


if __name__ == "__main__":
    app.run()
