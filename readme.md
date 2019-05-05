# Enpass Database Exporter

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
[![GitHub contributors](https://img.shields.io/github/contributors/Naereen/StrapDown.js.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/contributors/)

This script makes it easy to sync an Enpass database between iOS/macOS and Windows devices.

## Getting Started

This is a simple script made for both private and business users that adopt Enpass Password Manager.

It is created to allow users to sync their password database between multiple Cloud services. In particular it makes it easy to sync an Enpass database between iOS/macOS and Windows devices.

It works with every version of Enpass below V6. Starting from V6, iCloud is supported by default on each platform.

Many users, especially the business ones, are not able to upgrade to Enpass V6 for various reasons. This script could be of help to all of them.

It is written in Python, hence I recommend to use it on a desktop environment. Tested on Windows 10, Ubuntu 18.04 and macOS 10.14. However it is meant for a Windows environment, of course.

## Deployment

1. Download the Master file directly from this repository [here](https://github.com/mniuop/enpass_db_exporter/archive/master.zip);
2. Extract the content with a tool like [7-Zip](https://www.7-zip.org/);
3. Run the scrypt;
4. ???
5. Profit.

## Tips

- Be sure to have [Python](https://www.python.org/) (better V3 and above) installed in your Windows OS. Otherwise, just go [here](https://www.python.org/downloads/windows/), download and install it.

- You can run this script manually everytime you update your Enpass database. You can also set the Windows Task Scheduler in order to run the script whenever you want, e.g.: once in the morning and once in the evening. The Windows Task Scheduler is highly customizable and you can find everything about it [here](https://docs.microsoft.com/en-us/windows/desktop/taskschd/task-scheduler-start-page).

- This script is really simple and full of comments ready to help you understand how it works. Moreover you can easily adapt it to your needs by changing the default paths that point to the database or to the Cloud provider of your choice.

## Built With

* [Python](https://www.python.org/) - The language used
* [PyCharm](https://www.jetbrains.com/pycharm/) - The IDE used to write the code
* [Kyte](https://kite.com/) - The AI Autocomplete tested for this project

## License

This project is licensed under the MIT License - see the [license.md](license.md) file for details.
