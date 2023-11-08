# Installation

## Install SDKMAN

*This is optional if you already have a working Java Development Kit (JDK) 
on your machine.*

Check your JDK installation:
```bash
java -version
```

[SDKMAN Installation Instructions](https://sdkman.io/install) (copied here)

```bash
curl -s "https://get.sdkman.io" | bash
```

Then it will load magic sdkman functions into your bash shell.

```bash
sdk list           # to see all possible JVM SDKs you can instsall
sdk list java      # to see all possible JDKs you can install
sdk install java   # install the default JDK
sdk install kotlin # install latest kotlin
sdk install gradle # install latest gradle (build tool for jvm projects)
```

On my machine `sdk list java` looked like this:
<img width="1250" alt="Screenshot 2023-10-11 at 10 30 45 AM" src="https://github.com/jazzyfresh/cmsi3801/assets/1182129/e20d03ec-c4e8-4656-8aab-4159eed74c14">

<img width="1245" alt="Screenshot 2023-10-11 at 10 30 25 AM" src="https://github.com/jazzyfresh/cmsi3801/assets/1182129/c75e782c-cf6c-4058-9ca0-690d578677f7">

The latest OpenJDK was not available for my CPU, so I had to install an older version.

<img width="1229" alt="Screenshot 2023-10-11 at 10 30 07 AM" src="https://github.com/jazzyfresh/cmsi3801/assets/1182129/19fd48c4-dc5a-4869-98db-8626c589c631">

<img width="1250" alt="Screenshot 2023-10-11 at 10 29 04 AM" src="https://github.com/jazzyfresh/cmsi3801/assets/1182129/c8b917ee-10ae-4c1f-ab45-f99596cba30d">

You can show the above installed binaries on your path
```bash
echo $PATH
```

If you try to see SDKMAN on your path, you will see it is not there. That is because of bash magic in `$HOME/.sdkman/bin/sdkman-init.sh`. This is why `which sdk` does not show anything.
<img width="1261" alt="Screenshot 2023-10-11 at 10 29 41 AM" src="https://github.com/jazzyfresh/cmsi3801/assets/1182129/17446a0d-9955-4b75-89fa-56dac6169171">



## Setup Kotlin IDEs

### IntelliJ IDEA
https://www.jetbrains.com/idea/download

Make sure to scroll down and download the Community Edition, which is free!
Otherwise you trial license of the Ultimate Edition will expire in a month.

Also make sure to choose the right binary for your CPU!

![Screenshot 2023-10-18 at 11 16 28 AM](https://github.com/jazzyfresh/cmsi3801/assets/1182129/b1d6848a-cb6f-4d98-b5f9-a0b5c42377fe)

![Screenshot 2023-10-18 at 11 28 18 AM](https://github.com/jazzyfresh/cmsi3801/assets/1182129/6d4d72b2-a7e7-45f8-af14-977a18604ea5)


### Android Studio

[Download](https://developer.android.com/studio)
[System Requirements](https://developer.android.com/studio/install)

Also make sure to choose the right binary for your CPU!

![Screenshot 2023-10-18 at 11 28 39 AM](https://github.com/jazzyfresh/cmsi3801/assets/1182129/3c17ac60-8b74-42d5-bee2-213e54dd75d0)


### VSCode

[Setup the Kotlin plugin to VSCode](https://in-kotlin.com/ide/vscode/setup-vscode-for-kotlin-development/)
