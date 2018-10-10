<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>${fig_id}</title>
        <script type="text/javascript" src="https://d3js.org/d3.v4.js"></script>
        <style>
            #tooltip {
                position: absolute;
                width: auto;
                height: auto;
                padding: 10px;
                background-color: white;
                border-radius: 10px;
                box-shadow: 4px 4px 10px rgba(0,0,0,0.4);
                pointer-events: none;
            }

            #tooltip.hidden {
                display: none;
            }

            #tooltip p {
                margin: 0;
                font-family: sans-serif;
                font-size: 16px;
                line-height: 20px;
            }
        </style>
    </head>
    <body>
        <div class="figure">
        <div id="tooltip" class="hidden">
            <div id="value"></div>
        </div>
        </div>
        <script type="text/javascript">

            var dataset = ${dataset}

            <%include file="/bubble.js" />

        </script>
    </body>
</html>   