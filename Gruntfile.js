/* global module:true */

module.exports = function (grunt) {
    'use strict';

    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        themePath: 'probe_project/local_static/',
        jshint: {
            options: {
                jshintrc: '.jshintrc'
            },
            gruntfile: {
                src: 'Gruntfile.js'
            }
        },
        clean: {
            dist: {
                src: ['<%= themePath %>js/app.js', '<%= themePath %>js/app.min.js']
            }
        },
        uglify: {
            dist: {
                src: '<%= themePath %>js/app.js',
                dest: '<%= themePath %>js/app.min.js'
            }
        },
        sass: {
            dist: {
                options: {
                    style: 'expanded'
                },
                files: {
                    '<%= themePath %>css/theme.css': '<%= themePath %>css/theme.scss'
                }
            }
        },
        watch: {
            gruntfile: {
                files: '<%= jshint.gruntfile.src %>',
                tasks: ['jshint:gruntfile']
            },
            sass: {
                files: ['**/*.scss'],
                tasks: ['sass']
            },
            theme: {
                files: '<%= themePath %>**/*',
                options: {
                    livereload: true
                }
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-jshint');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-clean');
    grunt.loadNpmTasks('grunt-contrib-sass');

    // Default task.
    grunt.registerTask('default', ['jshint', 'clean', 'sass', 'watch']);
};
