# CSV to SQL - A Handy CLI Utility

A simple little program that converts .csv data into an SQL insert command.

```diff
-Before Conversion-
column1, column2, column3
varchar1, 1, true
varchar2, 2, false

+After Conversion+
INSERT INTO table_name (column1, column2, column3) VALUES
('varchar1', 1, true),
('varchar2', 2, false);
```

While developing my web application, [Zeldle](https://github.com/ARHafer/Zeldle), I reached a point in development where I needed to populate a database table.
Rather than doing so by hand or using an existing program to automate the process, I took the opportunity to learn Python and build the tool myself.

This project was my introduction to Python and an interesting learning experience, especially coming from Java.

In its current state, the program:
* Validates .csv structure.
* Streams .csv data via generators.
* Formats data depending on specified data type.
* Prints SQL insert commands into the console.


## How to Use
Using this program is very simple. Upon starting it will prompt you for:

* The path of your .csv file.
* The data type of each column. (*It's multiple choice, don't worry...*)
* The name of the table you wish to insert the data into.

After inputting this information, your insert command will be printed into the console!


## Future Versions?
I may come back and update this program someday as an excuse to refine my ability in Python.

### Possible Future Additions

* Improved handling of SQL formatting edge cases such as empty values and apostrophes.
* Exporting generated commands to .sql file.
* Support for different file formats such as .json or .xml.
* Smoother user experience in general.
