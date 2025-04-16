from flask import Flask, render_template, request, redirect, url_for, make_response


# instantiate the app
app = Flask(__name__)

# create category list
categories = [
    [1, "Kid Fiction"],
    [2, "Preschool Reading"],
    [3, "Crafts and Hobbies"],
    [4, "Textbook"]
]

# create book list
books = [
    [1, 1, "Wave of the Sea Dragon", "Tracey West", "13-9781338635485", 5.99, "Wave-of-the-Sea-Dragon.png", 1],
    [2, 1, "Aven Green Sleuthing Machine", "Dusti Bowling", "13-9781454942214", 0.99, "Aven-Green-Sleuthing-Machine.png", 1],
    [3, 1, "The Bad Guys", "Aaron Blabey", "13-9780545912402", 0.99, "Bad-Guys.png", 0],
    [4, 1, "CatStronauts: Robot Rescue", "Drew Brockington", "13-9780316307567", 8.99, "Robot-Rescue.png", 1],

    [5, 2, "Giraffes Can't Dance", "Giles Andreae", "13-9781338031188", 0.99, "Giraffes-Cant-Dance.png", 1],
    [6, 2, "Dr. Seuss's ABC", "Dr Seuss", "13-9780679882817", 4.99, "ABC.png", 1],
    [7, 2, "Alphablock", "Christopher Franceschelli, Peski Studio", "13-9781419709364", 16.99, "Alphablock.png", 0],
    [8, 2, "First 100 Words", "Roger Priddy", "13-9780312510787", 5.99, "100-Words.png", 1],

    [9, 3, "The Complete Baking Book for Young Chefs", "America's Test Kitchen Kids", "13-9781492677697", 1.35, "Complete-Baking-Book.png", 1],
    [10, 3, "Easy Origami", "John Montroll", "13-9780486272986", 4.48, "Easy-Origami.png", 1],
    [11, 3, "Mermaid Coloring Book", "Silly Bear", "13-9781913671198", 5.99, "Mermaid-Coloring-Book.png", 0],
    [12, 3, "Mazes for Kids", "Zoey Bird", "13-9798668012374", 9.99, "Mazes-for-Kids.png", 1],

    [13, 4, "Ultimate Grade 2 Math Workbook", "IXL Learning", "13-9781947569492", 5.26, "Ultimate-Grade2-Math.png", 1],
    [14, 4, "Ultimate Grade 3 Math Workbook", "IXL Learning", "13-9781947569508", 2.50, "Ultimate-Grade3-Math.png", 1],
    [15, 4, "Ultimate Grade 6 Math Workbook", "IXL Learning", "13-9781947569614", 6.50, "Ultimate-Grade6-Math.png", 0],
    [16, 4, "Ultimate Grade 4 Math Workbook", "IXL Learning", "13-9781947569515", 4.82, "Ultimate-Grade4-Math.png", 1]
]


# set up routes
@app.route('/')
def home():
    #Link to the index page.  Pass the categories as a parameter
    return render_template("index.html", categories=categories)

@app.route('/category')
def category():
    try:
        selectedCategoryId = int(request.args.get("category"))
        selectedBooks = [b for b in books if b[1] == selectedCategoryId]
        return render_template("category.html", categories=categories, books=selectedBooks, selectedCategory=selectedCategoryId)
    except Exception as e:
        return render_template("error.html", error=str(e))

@app.route('/search')
def search():
    try:
        query = request.form.get("search", "").lower()
        foundBooks = [b for b in books if query in b[2].lower()]
        return render_template("category.html", categories=categories, books=foundBooks, selectedCategory=None)
    except Exception as e:
        return render_template("error.html", error=str(e))

@app.errorhandler(Exception)
def handle_error(e):
    """
    Output any errors - good for debugging.
    """
    return render_template("error.html", error=str(e)) # render the edit template


if __name__ == "__main__":
    app.run(debug = True)
