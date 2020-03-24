define({ "api": [
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "./apidoc/main.js",
    "group": "/home/cristina/PycharmProjects/jwt-auth-test/apidoc/main.js",
    "groupTitle": "/home/cristina/PycharmProjects/jwt-auth-test/apidoc/main.js",
    "name": ""
  },
  {
    "type": "DELETE",
    "url": "/api/v1/profile/",
    "title": "Delete user's profile",
    "version": "1.0.0",
    "name": "DeleteProfile",
    "group": "Authentication",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "token",
            "description": "<p>The users API token in the format &quot;Token {token}&quot;.</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>User's id.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "message",
            "description": "<p>Profile is deleted.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n    {\n        'remove profile message': 'Your profile is successfully deleted'\n    }",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "InternalServerError 500": [
          {
            "group": "InternalServerError 500",
            "type": "Object",
            "optional": false,
            "field": "InternalServerError",
            "description": ""
          }
        ]
      }
    },
    "filename": "./run.py",
    "groupTitle": "Authentication"
  },
  {
    "type": "GET",
    "url": "/api/v1/profile/",
    "title": "Get user information",
    "version": "1.0.0",
    "name": "GetProfile",
    "group": "Authentication",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "token",
            "description": "<p>The users API token in the format &quot;Token {token}&quot;.</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "secret",
            "description": "<p>User's secret.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "secret",
            "description": "<p>User's secret.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"secret message\": \"I like penguins\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "InternalServerError 500": [
          {
            "group": "InternalServerError 500",
            "type": "Object",
            "optional": false,
            "field": "InternalServerError",
            "description": ""
          }
        ]
      }
    },
    "filename": "./run.py",
    "groupTitle": "Authentication"
  },
  {
    "type": "PATCH",
    "url": "/api/v1/profile/",
    "title": "Update user's secret",
    "version": "1.0.0",
    "name": "PatchProfile",
    "group": "Authentication",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "token",
            "description": "<p>The users API token in the format &quot;Token {token}&quot;.</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "new_secret",
            "description": "<p>User's secret input.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "new_secret",
            "description": "<p>User's new secret.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n    {\n        \"updated secret message\": \"I also like cats\"\n    }",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "InternalServerError 500": [
          {
            "group": "InternalServerError 500",
            "type": "Object",
            "optional": false,
            "field": "InternalServerError",
            "description": ""
          }
        ]
      }
    },
    "filename": "./run.py",
    "groupTitle": "Authentication"
  },
  {
    "type": "POST",
    "url": "/api/v1/login/",
    "title": "User login",
    "version": "1.0.0",
    "name": "PostLogin",
    "group": "Authentication",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": "<p>User's username.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>User's password.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "token",
            "description": "<p>User's jwt.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"token\": \"eyJ0eXA...\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Unauthorized 401": [
          {
            "group": "Unauthorized 401",
            "type": "Object",
            "optional": false,
            "field": "InvalidLogin",
            "description": "<p>Username or password is incorrect.</p>"
          }
        ]
      }
    },
    "filename": "./run.py",
    "groupTitle": "Authentication"
  },
  {
    "type": "POST",
    "url": "/api/v1/registration/",
    "title": "User registration",
    "version": "1.0.0",
    "name": "PostRegistration",
    "group": "Authentication",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "allowedValues": [
              "\"\\w\""
            ],
            "optional": false,
            "field": "username",
            "description": "<p>User's username.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "size": "8..",
            "optional": false,
            "field": "password",
            "description": "<p>User's password.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>User's email.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "welcomeMessage",
            "description": "<p>Personalised welcome message</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    'welcome message': 'Thank you for joining Cristina23'\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Unauthorized 401": [
          {
            "group": "Unauthorized 401",
            "type": "Object",
            "optional": false,
            "field": "InvalidPassword",
            "description": ""
          },
          {
            "group": "Unauthorized 401",
            "type": "Object",
            "optional": false,
            "field": "InvalidUsername",
            "description": ""
          },
          {
            "group": "Unauthorized 401",
            "type": "Object",
            "optional": false,
            "field": "UnavailableUsername",
            "description": ""
          },
          {
            "group": "Unauthorized 401",
            "type": "Object",
            "optional": false,
            "field": "InvalidEmailFormat",
            "description": ""
          }
        ],
        "InternalServerError 500": [
          {
            "group": "InternalServerError 500",
            "type": "Object",
            "optional": false,
            "field": "InternalServerError",
            "description": ""
          }
        ]
      }
    },
    "filename": "./run.py",
    "groupTitle": "Authentication"
  }
] });
