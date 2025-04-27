# Grazioso-Salvare-Dashboard

# Reflection Questions

- How do you write programs that are maintainable, readable, and adaptable?
In this project, maintainability was achieved by separating concerns: the AnimalShelter.py file contained all database interaction logic as a reusable CRUD class​
, while the dashboard (ProjectTwo.ipynb) focused solely on user interface and visualization. Methods are clearly named (create, read, update, delete), comments were added where necessary, and variables use consistent, descriptive naming conventions. This modular approach allowed changes in the database layer without needing to modify dashboard logic.

Working this way provided the advantage of easy debugging, future reusability, and separation of database responsibilities from the front-end display. In the future, I could easily reuse the AnimalShelter class to connect other dashboards or expand functionality to new projects involving MongoDB.

# How do you approach a problem as a computer scientist?
I approached the Grazioso Salvare project by breaking it into small, logical steps:

- First ensuring the database connection worked through CRUD testing.

- Then building an unfiltered data table.

- Gradually layering in filter logic, chart visualizations, and row selection functionality.

Compared to past courses, I relied much more heavily on incremental testing at every step, rather than building everything first and debugging later. Moving forward, I would continue this agile approach: building a feature, testing it, and only then adding the next layer. It reduces overall debugging time and leads to a cleaner final product.

# What do computer scientists do, and why does it matter?
Computer scientists build systems that solve real-world problems through automation, optimization, and data analysis. In this project, my work empowered Grazioso Salvare to rapidly identify ideal candidates for rescue training, saving valuable time that could be spent on training and rescues rather than data entry and manual search.

Beyond this project, dashboards like this allow organizations to make data-driven decisions more efficiently, which is critical in industries where time, accuracy, and quick response can save lives.
