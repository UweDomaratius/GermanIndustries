/**
 * @type {import('semantic-release').GlobalConfig}
 */
module.exports = {
  branches: ["main"],
  plugins: [
	"@semantic-release/commit-analyzer",
	"@semantic-release/release-notes-generator",
	["@semantic-release/github",
	  {
	    "assets": [
		  { "path": "german_industries.zip", "label": "German Industries set" }
		]
	  }
	]
  ]
};