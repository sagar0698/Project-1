from flask import Flask, request, jsonify
import sqlite3
import logging

#Authenicating User
@app.route('/login', methods = ['POST'])
def authenicateUser():
    username = query_parameters.get('username')
    password = query_parameters.get('password')

    #create db 

    hashed_password = result[0].get('password')
    return jsonify(check_password_hash(hashed_password, password))

#Allowing a user to follower others
@app.route('/follower', methods = ['POST'])
def addFollower():
    username = query_parameters.get('username')
    addFollower = query_parameters.get('addFollower')

#Allowing a user to unfollow others
@app.route('/unfollow', methods = ['DELETE'])
def unfollowUser():
    username = query_parameters.get('username')
    unfollowUser = query_parameters.get('unfollowUser')
