# Qwiklabs Assessment: Automatically Generate a PDF and send it by Email

## Project Problem Statement

It's that time again, time to flex your programming muscles and practice solving a real-life problem with the skills you acquired!

In the next lab, you'll have to process information related to the sales your company generated last month, and turn that into a nicely formatted PDF report that you'll then send by email so that your boss can look at it. The lab machine has email configured so that you can check your resulting emails through a nice webmail interface that's already up and running.

The system that you'll work with already includes some scripts that will do part of the work for you. You'll need to put these pieces together to get the result you want, basing your code on the one that's already there.

As we called out before, solving these problems can take some time, and that's ok! Solving complex problems is the best way to really master your coding skills. Before you start the lab, make sure you understand what you need to do and that you know how you want to solve it. Nobody is rushing you, so take as much time as you need, review any concepts that are not totally clear, and then get to it.

Good luck, you can totally do this!

## Introduction

You work for a company that sells second hand cars. Management wants to get a summary of the amounts of vehicles that have been sold at the end of every month. The company already has a web service which serves sales data at the end of every month but management wants an email to be sent out with an attached PDF so that data is more easily readable.

## What you’ll do

-   Write a script that summarizes and processes sales data into different categories
-   Generate a PDF using Python
-   Automatically send a PDF by email

You'll have 90 minutes to complete this lab.

## Sales summary

In this section, let's view the summary of last month's sales for all the models offered by the company. This data is in a JSON file named car_sales.json. Let's have a look at it.

```bash
cat car_sales.json
```

<!-- Image from source -->

![[car_sales.json](](https://cdn.qwiklabs.com/A2aAqrGDdDqk0sbLXhXAl%2FluSkUdrypVdWv5qYyRgwo%3D)

To simplify the JSON structure, here is an example of one of the JSON objects among the list.

```bash
{
        "id": 47,
        "car": {
                "car_make": "Lamborghini",
                "car_model": "Murciélago",
                "car_year": 2002
        },
        "price": "$13724.05",
        "total_sales": 149
}
```

Here `id`, `car`, `price` and `total_sales` are the field names (key).

The script `cars.py` already contains part of the work, but learners need to complete the task by writing the remaining pieces. The script already calculates the car model with the most revenue (price \* total_sales) in the process_data method. Learners need to add the following:

1. Calculate the car model which had the most sales by completing the process_data method, and then appending a formatted string to the summary list in the below format:

-   "The {car model} had the most sales: {total sales}"

2. Calculate the most popular car_year across all car make/models (in other words, find the total count of cars with the car_year equal to 2005, equal to 2006, etc. and then figure out the most popular year) by completing the process_data method, and append a formatted string to the summary list in the below format:

-   "The most popular year was {year} with {total sales in that year} sales."

### The challenge

Here, you are going to update the script cars.py. You will be using the above JSON data to process information. A part of the script is already done for you, where it calculates the car model with the most revenue (price \* total_sales). You should now fulfil the following objectives with the script:

1. Calculate the car model which had the most sales.
   a. Call format_car method for the car model.

2. Calculate the most popular car_year across all car make/models.
    > Hint: Find the total count of cars with the car_year equal to 2005, equal to 2006, etc. and then figure out the most popular year.

Grant required permissions to the file cars.py and open it using nano editor.

```bash
sudo chmod o+wx ~/scripts/cars.py
nano ~/scripts/cars.py
```

The code is well commented including the TODO sections for you to understand and fulfill the objectives.

### Generate PDF and send Email

Once the data is collected, you will also need to further update the script to generate a PDF report and automatically send it through email.

To generate a PDF:

-   Use the reports.generate() function within the main function.
-   The report should be named as cars.pdf, and placed in the folder /tmp/.
-   The PDF should contain:
    -   A summary paragraph which contains the most sales/most revenue/most popular year values worked out in the previous step.
        > Note: To add line breaks in the PDF, use: <br/> between the lines.
    -   A table which contains all the information parsed from the JSON file, organised by id_number. The car details should be combined into one column in the form <car_make> <car_model> (<car_year>).
        > Note: You can use the cars_dict_to_table function for the above task.
        > Example:
        <!-- table -->
        | **ID** | **Car**              | **Price** | **Total Sales** |
        | ------ | -------------------- | --------- | --------------- |
        | 47     | Acura TL (2007)      | €14459,15 | 1192            |
        | 73     | Porsche 911 (2010)   | €6057,74  | 882             |
        | 85     | Mercury Sable (2005) | €45660,46 | 874             |

To send the PDF through email:

Once the PDF is generated, you need to send the email, using the `emails.generate()` and `emails.send()` methods.

Use the following details to pass the parameters to `emails.generate()`:

-   **From**: automation@example.com
-   **To**: <user>@example.com
-   **Subject line**: Sales summary for last month
-   **E-mail Body**: The same summary from the PDF, but using \n between the lines
-   **Attachment**: Attach the PDF path i.e. generated in the previous step

Once you have completed editing cars.py script, save the file by typing **Ctrl-o**, **Enter** key, and **Ctrl-x**.

Run the `cars.py` script, which will generate mail to their user.

```bash
./scripts/cars.py
```

Now, check the webmail for any new mail. You can click on the Refresh button to refresh your inbox.

Output:
![](https://cdn.qwiklabs.com/EGbZxG2RRNc%2F%2B70k%2FDDPpXB1l6Wza4ZSNTZba4rdYWo%3D)
Open `cars.pdf` that's located on the right most side.
![](https://cdn.qwiklabs.com/pPYYMs48r3Z3qP7wkDJqi6uiOj%2F3YMtC8%2BH0wAhC0AA%3D)

## Optional challenge

As **optional** challenges, you could try some of the following functionalities:

1. Sort the list of cars in the PDF by total sales.

2. Create a pie chart for the total sales of each car made.

3. Create a bar chart showing total sales for the top 10 best selling vehicles using the [ReportLab Diagra library](https://www.reportlab.com/software/diagra/). Put the vehicle name on the X-axis and total revenue (remember, price \* total sales!) along the Y-axis.
