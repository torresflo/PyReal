![GitHub license](https://img.shields.io/github/license/torresflo/PyReal.svg)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
![GitHub contributors](https://img.shields.io/github/contributors/torresflo/PyReal.svg)
![GitHub issues](https://img.shields.io/github/issues/torresflo/PyReal.svg)

<p align="center">
  <h1 align="center">PyReal</h3>

  <p align="center">
    A little API to retrieve data and photos from the social netwotk BeReal.
    <br />
    <a href="https://github.com/torresflo/PyReal/issues">Report a bug or request a feature</a>
  </p>
</p>

## Table of Contents

* [Getting Started](#getting-started)
  * [Prerequisites and dependencies](#prerequisites-and-dependencies)
  * [Installation](#installation)
* [Usage](#usage)
  * [API](#API)
  * [Application](#application)
  * [Troubleshooting](#troubleshooting)
* [Examples](#examples)
* [Contributing](#contributing)
* [License](#license)

## Getting Started

For users, you can just download the latest release and run it! 
Following information are mainly for developers.

### Prerequisites and dependencies

This repository is tested with Python 3.7+.

You should install PyReal in a [virtual environment](https://docs.python.org/3/library/venv.html). If you're unfamiliar with Python virtual environments, check out the [user guide](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).
First, create a virtual environment with the version of Python you're going to use and activate it.

Then, you will need to install the dependencies of the project:

```bash
pip install -r requirements.txt
```

### Installation

Follow the instructions above then clone the repo (`git clone https:://github.com/torresflo/PyReal.git`). You can now run `main.py` to test the API or just write your own application.

## Usage

### API

The API is currently in development. 

The goal of the API is to be able to retrieve data from BeReal (read-only), it is not planned to add write features like posting a photo or creating a comment.

Here are the current implemented and planned features:
- [x] Past posted photos (Memories)
- [ ] Profile and User info
- [ ] Current Feed (Friends and Discovery)
- [ ] Memories Video
- [ ] Reactions (RealMojis)

### Application

A small application (`main.py`) can be used to access the features.

On the first launch, it will ask for your phone number in the <a href="https://en.wikipedia.org/wiki/E.164">E614 format</a>: `+[country code][number]`.
Then it will ask you to enter the OTP (one time password) that you will receive on this phone number. This will allow the program to retreive your token and establish the connection with BeReal under your account.

> :warning: Your token will be stored in `saved\token.txt`, do not share it!

With the current version, the program will automatically download all your posted photos (Memories). Images are stored in `saved\photos` and are composed of both the front and back photos of each post.

### Troubleshooting

A common issue is to fail to send the phone number at the first step. This is usually due because quota was exceeded in the BeReal API. In this case, just retry until it works (it could take a couple of retry).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the GNU General Public License v3.0. See `LICENSE` for more information.