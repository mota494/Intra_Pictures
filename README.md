<div align="center">

# Intra Pictures

## Description

</div>

This is a very simple way to get students and pisciners photos from Intra, the platform used by the 42 School.

---

<div align="center">

## Requirements

</div>

For this to work you'll need:

- A 42 school staff account
- GNU Make
- A C compiler
- Python 3
- beautifulsoup `pip3 install beautifulsoup4` 
- selenium `pip3 install selenium`
- Google Chrome

<div align="center">

## How to use

</div>

To start, head over to the users manager page on your intra admin tools and use the filters to set the range of students that you want to pull the images.

After you download the file in a .csv format, rename it to `users.csv` and paste it on the root folder of this repository.

When you're done with that just run the Makefile with `Make`.

After the program has started it will prompt you to fill out your intra credentials, this **doesn't** need to be an admin account 

If you filled out the credentials correctly it will open up a **Google Chrome** window where it will run the script, just leave it while it's doing it's thing

When it's done it will close and leave on the root folder of this repo a file named `final.csv` that will have every link to the students images that can then be used on google sheets per example
