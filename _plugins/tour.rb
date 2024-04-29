module Jekyll 
    module TourPlugin
        class TourPageGenerator < Jekyll::Generator
            safe true
            priority :low

            def generate(site)
                site.collections['routes'].docs.each do |route|
                    raise "Route must have a slug" if route.data['slug'].nil?
                    if route.data['origin'] == nil 
                        route.data['origin']= route.data['slug'].split("-").first
                    end 
                    if route.data['destination'] == nil
                        route.data['destination']= route.data['slug'].split("-").last
                    end
                end
                        
                # Generate the tour page
                site.collections['origins'].docs.each do |origin|
                    # site.pages << OriginPage.new(site, origin)
                    site.collections['destinations'].docs.each do |destination|
                        site.pages << TourPage.new(site, origin, destination)
                    end
                end
            end
        end
        class TourPage < Jekyll::Page
            def initialize(site, origin, destination)
                raise "Origin and Destination must be different" if origin.data['slug'] == destination.data['slug']
                raise "Origin should be nonempty" if origin.data['slug'].empty?
                raise "Destination should be nonempty" if destination.data['slug'].empty?
                @site = site
                @base = site.source
                @dir = "#{origin.data['slug']}/#{destination.data['slug']}"
                @permalink = "/#{@dir}/"
                # All pages have the same filename, so define attributes straight away.
                @basename = 'index'      # filename without the extension.
                @ext      = '.html'      # the extension.
                @name     = 'index.html' # basically @basename + @ext.
                @data =  {
                    "title" => "Travel Instruction from #{origin.data['title']} to #{destination.data['title']}",
                    "origin"=> origin.data['slug'],
                    "destination"=> destination.data['slug'],
                    "layout"=> "tour",
                    # "nav_exclude"=> true,
                    "parent"=> origin.data['title']

                } 
            end
        end
        # class OriginPage < Jekyll::Page
        #     def initialize(site, origin)
        #         @site = site
        #         @base = site.source
        #         @dir = "#{origin.data['slug']}"
        #         @permalink = "/#{@dir}/"
        #         # All pages have the same filename, so define attributes straight away.
        #         @basename = 'index'      # filename without the extension.
        #         @ext      = '.html'      # the extension.
        #         @name     = 'index.html' # basically @basename + @ext.
        #         @data =  {
        #             "title" => "#{origin.data['title']}",
        #             "origin"=> origin.data['slug'],
        #             "layout"=> "origin"
        #         }
        #         @content = origin.content
        #     end
        # end
    end
end