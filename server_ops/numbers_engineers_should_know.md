# Numbers that Engineers Should Know

## Latency Numbers Every Programmer Should Know

[webpage](https://samwho.dev/numbers/?fo)

- L1 cache reference: 1 ns
- Branch mispredict: 3 ns
- L2 cache reference: 4 ns
- Mutex lock/unlock: 17 ns
- 1 KB data fetch via 1 Gbps network: 44 ns
- Main memory reference: 100 ns
- Compress 1 KB with Zippy: 2 µs
- 1 MB data sequential fetch via Memory: 3 µs
- random 4K read (SSD): 16 µs
- 1 MB sequential read (SSD): 49 µs
- round trip within the same data center: 500 µs
- 1 MB sequential read (disk): 825 µs
- disk seek: 2 ms
- round trip California to Netherlands: 150 ms

## Latency Numbers Every Web Programmer Should Know

[vercel: Latency Numbers Every Web Developer Should Know](https://vercel.com/blog/latency-numbers-every-web-developer-should-know)

| Metric | Estimated Latency | Metric Impact |
| --- | --- | --- |
| Wifi latency to internetWifi adds minimal latency to a connection. This can increase with a weak signal or older hardware. | 1-4ms | TTFB, FCP, LCP |
| 5G high-band (millimeter wave) latency to internetMillimeter wave is the fastest deployed mobile technology. However, it is only practical to use in dense urban areas with a line of sight to the radio tower. | 1-5ms | TTFB, FCP, LCP |
| User-space budget per frame for 60 frames per secondOn a 60fps device, a frame is painted every 16ms. However, the device needs some time for the actual processing of the frame. The time here is the time available for your code to compute what should be painted. | 5-10ms | Smooth framerate |
| 5G mid-band latency to internetThis is the regular 5G latency. Experience may vary in case of bad signal or an overloaded tower. | 10-30ms | TTFB, FCP, LCP |
| Round trip latency to a service or database in same cloud regionThis is the latency to a different service that is deployed close to you without going to the internet. | 10ms | TTFB, FCP, LCP |
| LTE latency to internetTypical latency for LTE, aka 4G cellular networks. | 15-50ms | TTFB, FCP, LCP |
| Frame-duration at 60 frames per second60 frames per second is the most popular frame rate for display devices. However, some newer devices support higher frame rates like 90 or 120 fps. | 16ms | Smooth frame rate |
| Round trip latency to other city on the same continentThis is the latency you can expect if you deploy to a region on the same continent as your user. It's calculated for a distance of 5000 kilometers, so the actual latency may be slightly higher or lower. | 33ms | TTFB, FCP, LCP |
| Shortest duration of time perceived by humans as time having passedWhen responding to user input, staying below this duration means that your user will perceive the response as instant. Citation | 40-80ms | INP |
| Time to parse 1MB of CSSParsing CSS is part of the work the browser has to perform to render a web page. | 100ms | FCP, LCP |
| Time to parse 1MB of HTMLParsing HTML is part of the work the browser has to perform to render a web page. While it is often negligible for shorter web pages, it can become a major factor for very long articles. | 120ms | FCP, LCP |
| 3G latency to internet3G is the slowest cellular standard in common use today. | 150ms | TTFB, FCP, LCP |
| Round trip latency to other side of earth with a high quality network (cold potato routing)This is the worst-case latency you should see if you deploy a service to a single region. | 150ms | TTFB, FCP, LCP |
| Time to parse 1MB of JSParsing JavaScript can have a major impact on page load time as it often grows more quickly than CSS and JS. Code-splitting is the primary technique to minimize JS size. | 150ms | FCP, LCP, INP |
| Duration of time perceived by humans as sluggishWhen reacting to user input, a response slower than this value will be perceived as having to wait. 200ms is also the threshold for "Needs improvement" in INP. | 200ms | INP |
| Round trip latency to other side of earth without leased fiber (hot potato routing)When users directly connect to a faraway server or when using a low-cost CDN, then latencies for users may double from passing bytes through the cheapest path possible. | 300ms | TTFB, FCP, LCP |
