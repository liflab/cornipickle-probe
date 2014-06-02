/* global module:true */

module.exports = function(grunt){
    'use strict';

    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        themePath: 'local_static/',
        jshint: {
            options: {
                jshintrc: '.jshintrc'
            },
            gruntfile: {
                src: 'Gruntfile.js'
            },
            js: {
                beforeconcat: ['<%= themePath %>js/lib/*.js'],
                afterconcat: ['<%= themePath %>js/app.js', '<%= themePath %>js/app.min.js']
            }
        },
        clean: {
            dist: {
                src: ['<%= themePath %>js/app.js', '<%= themePath %>js/app.min.js']
            }
        },
        concat: {
            options: {
                stripBanners: true,
                banner: '/*! <%= pkg.name %> - <%= grunt.template.today("yyyy-mm-dd") %> */\n\n'
            },
            dist: {
                src: ['<%= themePath %>js/lib/*.js'],
                dest: '<%= themePath %>js/app.js'
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
            lib: {
                files: ['<%= jshint.js.beforeconcat %>', '!<%= themePath %>js/app.js', '!' + '<%= themePath %>js/app.min.js'],
                tasks: ['jshint:js', 'clean:dist', 'concat:dist', 'uglify:dist']
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
    grunt.registerTask('default', ['watch']);

};
