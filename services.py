from flask import Flask, request, jsonify
import sqlite3

#Get user timeline
@app.route('/getUserTimeline', methods = ['GET'])
def getUserTimeline():
    username = query_parameters.get('username')
    query_parameters.getTweets

    return jsonify(getUserTimeline)

#Get public timeline
@app.route('/getPublicTimeline', methods = ['GET'])
def getPublicTimeline():
    getUsername = query_parameters.get('getUsername')
    query_parameters.getTweets

    return jsonify(getPublicTimeline)


#Get followers timeline
@app.route('/getFollowerTimeline', methods = ['GET'])
def getFollowerTimeline():
    username = query_parameters.get('username')
    follower = query_parameters.get('follower')

    return jsonify(getFollowerTimeline)

@app.route('/postTweet', methods = ['POST'])
def postTweet():
    query_parameters = request.form
    username = query_parameters.get('username')
    text = query_parameters.get('text')

    return jsonify(postTweet)
