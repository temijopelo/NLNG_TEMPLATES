def sds_generation_completed_email(month, year, view_sds_link):
    return f""" <!doctype html>
<html>
  <body>
    <div
      style='background-color:#F5F5F5;color:#262626;font-family:"Helvetica Neue", "Arial Nova", "Nimbus Sans", Arial, sans-serif;font-size:16px;font-weight:400;letter-spacing:0.15008px;line-height:1.5;margin:0;padding:32px 0;min-height:100%;width:100%'
    >
      <table
        align="center"
        width="100%"
        style="margin:0 auto;max-width:600px;background-color:#FAFAFA"
        role="presentation"
        cellspacing="0"
        cellpadding="0"
        border="0"
      >
        <tbody>
          <tr style="width:100%">
            <td>
              <div style="padding:16px 24px 16px 24px;background-color:#e8f0f0">
                <img
                  alt="Sample product"
                  src="https://pouch.jumpshare.com/preview/j2OHpNjxoY5cdnK42kh04okk4lYhialWELU9Voc4AidUnWVTzrAkLws0wcZ-7OGc2cWq9vuQLLMgczup72392EAFtBShOikdRJ0JuyX-yJ4"
                  style="outline:none;border:none;text-decoration:none;vertical-align:top;display:inline-block;max-width:100%"
                />
              </div>
              <div style="background-color:#e8f0f0;padding:0px 56px 32px 40px">
                <div
                  style="background-color:#FFFFFF;border-radius:12px;padding:16px 24px 24px 24px"
                >
                  <div
                    style='color:#2563EB;font-size:18px;font-family:Charter, "Bitstream Charter", "Sitka Text", Cambria, serif;font-weight:bold;padding:12px 24px 0px 24px'
                  >
                    SDS Generation Completed
                  </div>
                  <div
                    style="font-size:12px;font-weight:normal;padding:16px 24px 16px 24px"
                  >
                    SDS report for {month} {year} has been created on the ADPLNG_{year}.
                    Kindly confirm the buyers&#x27; financial capability.
                  </div>
                  <div style="text-align:center;padding:16px 24px 16px 24px">
                    <a
                      href="{view_sds_link}"
                      style="color:#FFFFFF;font-size:11px;font-weight:bold;background-color:#477606;border-radius:4px;display:inline-block;padding:12px 20px;text-decoration:none"
                      target="_blank"
                      ><span
                        ><!--[if mso
                          ]><i
                            style="letter-spacing: 20px;mso-font-width:-100%;mso-text-raise:30"
                            hidden
                            >&nbsp;</i
                          ><!
                        [endif]--></span
                      ><span>View SDS</span
                      ><span
                        ><!--[if mso
                          ]><i
                            style="letter-spacing: 20px;mso-font-width:-100%"
                            hidden
                            >&nbsp;</i
                          ><!
                        [endif]--></span
                      ></a
                    >
                  </div>
                </div>
                <div
                  style="font-size:12px;font-weight:normal;text-align:center;padding:16px 72px 16px 68px"
                >
                  You have received this notification because you are a user of
                  the NLNG IVCO App
                </div>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </body>
</html>
"""
