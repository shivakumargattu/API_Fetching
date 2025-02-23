{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMEzdmBY/RFHKoTkU4kn6oh",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/shivakumargattu/Python_Codes/blob/main/Python_pynb.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "haxwLZH1nnIx",
        "outputId": "af928f60-42f1-495d-9453-463fbc27e287"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Please Enter the word: shiva\n",
            "avihs\n"
          ]
        }
      ],
      "source": [
        "def reverseStr(word):\n",
        "  reverseWord=word[::-1]\n",
        "  return reverseWord\n",
        "userInput=input(\"Please Enter the word: \")\n",
        "result=reverseStr(userInput)\n",
        "print(result)\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# longest word in the santance\n",
        "def logngestWord(word):\n",
        "  longestword=\"\"\n",
        "  words=word.split(\" \")\n",
        "  for word in words:\n",
        "    if len(word)>len(longestword):\n",
        "      longestword=word\n",
        "  print(longestword)\n",
        "userInput=input(\"Please Enter the santance: \")\n",
        "logngestWord(userInput)\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9eaSuF_fyzPd",
        "outputId": "55864f73-8047-4b70-ecd9-b9e473b94754"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Please Enter the santance: Python is most easy to learn programming language\n",
            "programming\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# given String Palindrome or not\n",
        "\n",
        "def isPalindrome(word):\n",
        "  reverseWord=word[::-1]\n",
        "  if word==reverseWord:\n",
        "    print(\"Palindrome\")\n",
        "  else:\n",
        "    print(\"Not Palindrome\")\n",
        "userInput=input(\"Please Enter Word: \")\n",
        "isPalindrome(userInput)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_RN0jZqe3dz3",
        "outputId": "69243205-214f-4662-a01a-b73383346099"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Please Enter Word: zomoz\n",
            "Palindrome\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# without using indexing Palindrome\n",
        "\n",
        "userInput=input(\"Please Enter the word: \")\n",
        "reverseWord=\"\"\n",
        "for i in userInput:\n",
        "  reverseWord=i+reverseWord\n",
        "if userInput==reverseWord:\n",
        "  print(\"Palindrome\")\n",
        "else:\n",
        "  print(\"Not Palindrome\")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8h4dz76W4uWr",
        "outputId": "510a8e2c-21e6-4cea-ac8a-e1f540cd032b"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Please Enter the word: shiva\n",
            "Not Palindrome\n"
          ]
        }
      ]
    }
  ]
}